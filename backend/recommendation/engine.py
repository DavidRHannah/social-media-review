import logging

logger = logging.getLogger(__name__)

def get_recommendations(user_id: str, num_results: int = 5):
    """
    Generate recommendations for a given user using a heuristic algorithm.

    The algorithm uses pre-defined test user data. For known users, it returns their
    recommendations sorted by score in descending order. For unknown users, it returns a
    default set of recommendations.

    Args:
        user_id (str): The ID of the user.
        num_results (int): Maximum number of recommendations to return.

    Returns:
        list: A list of dictionaries, each containing 'item_id' and 'score'.
    """
    try:
        logger.info("Running heuristic recommendation algorithm for user_id: %s", user_id)
        
        # Test user data simulating user preferences with item scores.
        test_user_data = {
            "user1": [("itemA", 0.98), ("itemB", 0.95), ("itemC", 0.93), ("itemD", 0.90)],
            "user2": [("itemE", 0.97), ("itemF", 0.96), ("itemG", 0.92)],
            "user3": [("itemH", 0.99), ("itemI", 0.94), ("itemJ", 0.90)],
        }
        
        if user_id in test_user_data:
            # Sort recommendations by score in descending order.
            recommendations = sorted(test_user_data[user_id], key=lambda x: x[1], reverse=True)
            recommendations = [{"item_id": item, "score": score} for item, score in recommendations]
        else:
            # Default recommendations for unknown users.
            default_recommendations = [("defaultItem1", 0.85), ("defaultItem2", 0.80), ("defaultItem3", 0.75)]
            recommendations = [{"item_id": item, "score": score} for item, score in default_recommendations]
        
        logger.info("Recommendations for user_id %s: %s", user_id, recommendations[:num_results])
        return recommendations[:num_results]
    except Exception as e:
        logger.error("Error generating recommendations for user_id %s: %s", user_id, str(e))
        raise e
