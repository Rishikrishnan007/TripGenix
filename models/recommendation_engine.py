class HybridRecommendationEngine:
    def __init__(self, collaborative_model, content_based_model):
        """Initialize the hybrid recommendation engine with models."""
        self.collaborative_model = collaborative_model  # Collaborative Filtering Model
        self.content_based_model = content_based_model  # Content-Based Filtering Model

    def recommend(self, user_id, item_id, num_recommendations=5):
        """Generate recommendations based on user preferences and item features."""
        collaborative_recommendations = self.collaborative_model.recommend(user_id, num_recommendations)
        content_based_recommendations = self.content_based_model.recommend(item_id, num_recommendations)
        
        # Combine recommendations (this is a simple intersection; you can use more sophisticated methods)
        combined_recommendations = list(set(collaborative_recommendations) | set(content_based_recommendations))
        return combined_recommendations[:num_recommendations]

    def fit(self, data):
        """Fit the models with training data."""
        self.collaborative_model.fit(data)
        self.content_based_model.fit(data)
