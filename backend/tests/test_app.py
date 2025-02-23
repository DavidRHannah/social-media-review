import unittest
from app import create_app

class RecommendationAPITestCase(unittest.TestCase):
    def setUp(self):
        # Set up the Flask test client.
        self.app = create_app()
        self.client = self.app.test_client()
    
    def test_get_recommendations_valid_user1(self):
        # Test GET request for a known user (user1).
        response = self.client.get('/api/recommendations?user_id=user1&num_results=2')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["user_id"], "user1")
        self.assertEqual(len(data["recommendations"]), 2)
        for rec in data["recommendations"]:
            self.assertIn("item_id", rec)
            self.assertIn("score", rec)
    
    def test_get_recommendations_missing_user_id(self):
        # Test GET request missing the required user_id parameter.
        response = self.client.get('/api/recommendations?num_results=2')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("error", data)
    
    def test_post_recommendations_valid_user2(self):
        # Test POST request for a known user (user2).
        payload = {"user_id": "user2", "num_results": 3}
        response = self.client.post('/api/recommendations', json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["user_id"], "user2")
        self.assertEqual(len(data["recommendations"]), 3)
    
    def test_post_recommendations_invalid_json(self):
        # Test POST request with an invalid JSON payload.
        response = self.client.post('/api/recommendations', data="invalid json", content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn("error", data)

if __name__ == '__main__':
    unittest.main()
