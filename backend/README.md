
# Recommendation API Backend

This project provides a backend service for a recommendation engine built with Flask. The API exposes endpoints that allow the frontend (or any client) to request personalized recommendations via GET or POST methods.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [GET /api/recommendations](#get-apirecommendations)
  - [POST /api/recommendations](#post-apirecommendations)
- [Usage Examples](#usage-examples)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Prerequisites

- **Python 3.7+**
- **pip** (Python package installer)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://your-repository-url.git
   cd your-repository-directory
   ```

2. **Create and Activate a Virtual Environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To start the Flask development server, run:

```bash
python app.py
```

The server will start in debug mode on port `5000` by default and will be accessible at:  
`http://localhost:5000`

## API Endpoints

The API is served under the `/api` prefix.

### GET /api/recommendations

Fetches recommendations for a specific user.  
**Query Parameters:**

- `user_id` (required): The ID of the user.
- `num_results` (optional): Number of recommendations to return (default is 5).

**Example URL:**

```
http://localhost:5000/api/recommendations?user_id=123&num_results=3
```

### POST /api/recommendations

Accepts a JSON payload to fetch recommendations for a user.  
**JSON Payload:**

- `user_id` (required): The ID of the user.
- `num_results` (optional): Number of recommendations to return (default is 5).

**Example Payload:**

```json
{
  "user_id": "123",
  "num_results": 3
}
```

## Usage Examples

### GET Request Example

Using `curl`:

```bash
curl "http://localhost:5000/api/recommendations?user_id=123&num_results=3"
```

Expected Response:

```json
{
  "user_id": "123",
  "recommendations": [
    {"item_id": "A123", "score": 0.98},
    {"item_id": "B456", "score": 0.95},
    {"item_id": "C789", "score": 0.93}
  ]
}
```

### POST Request Example

Using `curl`:

```bash
curl -X POST "http://localhost:5000/api/recommendations" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "123", "num_results": 3}'
```

Expected Response:

```json
{
  "user_id": "123",
  "recommendations": [
    {"item_id": "A123", "score": 0.98},
    {"item_id": "B456", "score": 0.95},
    {"item_id": "C789", "score": 0.93}
  ]
}
```

## Troubleshooting

- **Server Not Starting:**  
  Ensure that all dependencies are installed and the correct version of Python is being used.

- **Invalid JSON Payload (POST):**  
  Make sure that the JSON payload is correctly formatted. Use a tool like [jsonlint](https://jsonlint.com/) to validate your JSON.

- **Missing Parameters:**  
  If you receive an error regarding missing `user_id`, double-check your query parameters or JSON payload.
