# recommendation_engine.py

class RecommendationEngine:
    def __init__(self, heuristics):
        """
        heuristics: a list of tuples (heuristic_function, weight)
        Each heuristic_function should take (user, item) and return a numeric score.
        """
        self.heuristics = heuristics

    def score_item(self, user, item):
        """Compute the composite score for a single item based on weighted heuristics."""
        score = 0.0
        for heuristic, weight in self.heuristics:
            score += weight * heuristic(user, item)
        return score

    def recommend(self, user, items, top_n=5):
        """
        Given a user and a list of items, return the top_n items based on their composite scores.
        """
        scored_items = [(item, self.score_item(user, item)) for item in items]
        scored_items.sort(key=lambda x: x[1], reverse=True)
        return [item for item, score in scored_items[:top_n]]


# Heuristic functions

def popularity_heuristic(user, item):
    """
    Returns the popularity score of the item.
    Assumes each item is a dict with a 'popularity' key.
    """
    return item.get("popularity", 0)

def interest_heuristic(user, item):
    """
    Returns 1 if the item’s category matches any of the user’s interests, else 0.
    Assumes the user dict contains an 'interests' list and the item dict contains a 'category'.
    """
    return 1.0 if item.get("category") in user.get("interests", []) else 0.0