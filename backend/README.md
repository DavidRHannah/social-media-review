# Recommendation API Backend

This repository provides a Flask-based backend service for a recommendation engine powered by a heuristic algorithm. The service exposes a RESTful API that returns recommendations based on pre-defined user data and includes comprehensive tests to ensure quality and reliability.

## Project Structure

```
project-root/
├── app.py                # Main application entry point.
├── recommendation/
│   └── engine.py         # Heuristic recommendation algorithm.
├── api/
│   └── routes.py         # API endpoint definitions.
├── tests/
│   └── test_app.py       # Unit tests for API endpoints.
├── requirements.txt      # List of dependencies.
└── README.md             # Project documentation.
```

## Prerequisites

- **Python 3.7+**
- **pip** (Python package installer)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://your-repository-url.git
   cd your-repository-directory
   ```

2. **Create and Activate a Virtual Environment (Recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the Flask development server:

```bash
python app.py
```

By default, the server runs in debug mode on [http://localhost:5000](http://localhost:5000).

## API Endpoints

All API endpoints are prefixed with `/api`.

### GET `/api/recommendations`

Fetch recommendations for a specific user.

**Query Parameters:**

- `user_id` (required): The ID of the user.
- `num_results` (optional): Number of recommendations to return (default is 5).

**Example:**

```bash
curl "http://localhost:5000/api/recommendations?user_id=user1&num_results=2"
```

**Expected Response:**

```json
{
  "user_id": "user1",
  "recommendations": [
    {"item_id": "itemA", "score": 0.98},
    {"item_id": "itemB", "score": 0.95}
  ]
}
```

### POST `/api/recommendations`

Submit a JSON payload to fetch recommendations.

**JSON Payload:**

- `user_id` (required): The ID of the user.
- `num_results` (optional): Number of recommendations to return (default is 5).

**Example:**

```bash
curl -X POST "http://localhost:5000/api/recommendations" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user2", "num_results": 3}'
```

**Expected Response:**

```json
{
  "user_id": "user2",
  "recommendations": [
    {"item_id": "itemE", "score": 0.97},
    {"item_id": "itemF", "score": 0.96},
    {"item_id": "itemG", "score": 0.92}
  ]
}
```

## Heuristic Recommendation Algorithm

The recommendation engine (in `recommendation/engine.py`) implements a heuristic algorithm:

- **Test Users:** For known users (e.g., `user1`, `user2`, `user3`), the engine returns a set of pre-defined recommendations sorted by score.
- **Unknown Users:** If the `user_id` is not recognized, a default set of recommendations is returned.

## Running Tests

The project includes industry-level tests using Python’s `unittest` framework. These tests cover both valid API calls and error conditions.

To run the tests, execute:

```bash
python -m unittest discover -s tests
```

This command will run all tests in the `tests` directory.

## Troubleshooting

- **Server Not Starting:**  
  Ensure that all dependencies are installed and that you are using Python 3.7 or higher.

- **Invalid JSON Payload:**  
  Verify that your POST requests contain correctly formatted JSON.

- **Missing Parameters:**  
  Ensure that the `user_id` parameter is provided in your requests.
