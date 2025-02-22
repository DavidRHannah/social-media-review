# tests.py

import unittest
from recommendation_engine import RecommendationEngine, popularity_heuristic, interest_heuristic

class TestRecommendationEngine(unittest.TestCase):
    def setUp(self):
        # Define a sample user and a list of items
        self.user = {"id": "user1", "interests": ["electronics", "books"]}
        self.items = [
            {"id": "item1", "category": "electronics", "popularity": 80},
            {"id": "item2", "category": "books", "popularity": 50},
            {"id": "item3", "category": "clothing", "popularity": 90},
            {"id": "item4", "category": "electronics", "popularity": 60},
            {"id": "item5", "category": "books", "popularity": 70},
        ]
        # Define our heuristics with weights: 70% popularity and 30% interest match
        heuristics = [
            (popularity_heuristic, 0.7),
            (interest_heuristic, 0.3)
        ]
        self.engine = RecommendationEngine(heuristics)

    def test_scoring(self):
        # Test score computation for a single item.
        item = {"id": "item1", "category": "electronics", "popularity": 80}
        # Expected score = 0.7 * 80 (popularity) + 0.3 * 1 (interest match) = 56 + 0.3 = 56.3
        expected_score = 0.7 * 80 + 0.3 * 1
        self.assertAlmostEqual(self.engine.score_item(self.user, item), expected_score)

    def test_recommend_order(self):
        # Test that recommendations are returned in the expected order.
        recommendations = self.engine.recommend(self.user, self.items, top_n=3)
        expected_order = ["item3", "item1", "item5"]
        result_ids = [item["id"] for item in recommendations]
        self.assertEqual(result_ids, expected_order)

    def test_edge_case_no_interest(self):
        # Test when a user has no interests; recommendations should be purely based on popularity.
        user = {"id": "user2", "interests": []}
        recommendations = self.engine.recommend(user, self.items, top_n=2)
        expected_order = ["item3", "item1"]
        result_ids = [item["id"] for item in recommendations]
        self.assertEqual(result_ids, expected_order)

if __name__ == "__main__":
    unittest.main()
