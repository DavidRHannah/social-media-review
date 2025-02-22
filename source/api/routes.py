from flask import Blueprint, request, jsonify, current_app
from recommendation.engine import get_recommendations

api = Blueprint('api', __name__)

@api.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    """
    API endpoint to fetch recommendations for a user.
    Supports both GET (via query parameters) and POST (with a JSON payload).

    Request Parameters:
      - user_id (string): The user ID for which recommendations are requested.
      - num_results (int, optional): Number of recommendations to return (default is 5).

    Returns:
        JSON response with user_id and a list of recommendations or an error message.
    """
    # Extract parameters from JSON body (POST) or query parameters (GET)
    if request.method == 'POST':
        data = request.get_json(force=True, silent=True)
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        user_id = data.get('user_id')
        num_results = data.get('num_results', 5)
    else:
        user_id = request.args.get('user_id')
        num_results = request.args.get('num_results', 5)

    # Validate required parameters.
    if not user_id:
        return jsonify({"error": "Parameter 'user_id' is required"}), 400

    # Ensure num_results is an integer.
    try:
        num_results = int(num_results)
    except ValueError:
        return jsonify({"error": "Parameter 'num_results' must be an integer"}), 400

    # Retrieve recommendations and return them.
    try:
        recs = get_recommendations(user_id, num_results)
        return jsonify({"user_id": user_id, "recommendations": recs}), 200
    except Exception as e:
        current_app.logger.error("Failed to get recommendations for user_id %s: %s", user_id, str(e))
        return jsonify({"error": "Internal server error"}), 500
