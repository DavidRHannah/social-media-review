from flask import Blueprint, request, jsonify, current_app
from recommendation.engine import get_recommendations

api = Blueprint('api', __name__)

@api.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    """
    API endpoint to fetch recommendations for a user.
    
    Supports:
      - GET requests via query parameters.
      - POST requests with a JSON payload.
    
    Request Parameters:
      - user_id (string, required): The ID of the user.
      - num_results (int, optional): Number of recommendations to return (default is 5).
    
    Returns:
      JSON response with the user_id and a list of recommendations or an error message.
    """
    if request.method == 'POST':
        data = request.get_json(force=True, silent=True)
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        user_id = data.get('user_id')
        num_results = data.get('num_results', 5)
    else:
        user_id = request.args.get('user_id')
        num_results = request.args.get('num_results', 5)
    
    if not user_id:
        return jsonify({"error": "Parameter 'user_id' is required"}), 400

    try:
        num_results = int(num_results)
    except ValueError:
        return jsonify({"error": "Parameter 'num_results' must be an integer"}), 400

    try:
        recs = get_recommendations(user_id, num_results)
        return jsonify({"user_id": user_id, "recommendations": recs}), 200
    except Exception as e:
        current_app.logger.error("Failed to get recommendations for user_id %s: %s", user_id, str(e))
        return jsonify({"error": "Internal server error"}), 500
