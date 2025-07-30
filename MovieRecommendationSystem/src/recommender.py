class Recommender:
    def __init__(self, user_matrix, similarity_df):
        """
        Initialize the Recommender with user-item ratings and user similarity data.

        Parameters:
        user_matrix (DataFrame): Matrix of user-item ratings with users as rows and movies as columns.
        similarity_df (DataFrame): User-user similarity matrix (e.g., cosine similarity).
        """
        self.user_matrix = user_matrix
        self.similarity_df = similarity_df

    def recommend_movies(self, user_id, top_n=5):
        """
        Generate top-N movie recommendations for a given user using user-based collaborative filtering.

        Parameters:
        user_id (int): ID of the user to generate recommendations for.
        top_n (int): Number of top recommendations to return. Default is 5.

        Returns:
        recommendations (Series or None): Series of recommended movie IDs with their weighted scores,
                                          or None if user not found or all movies are already seen.
        """
        #Return None if the user ID is not in the user matrix
        if user_id not in self.user_matrix.index:
            return None

        #Get similarity scores between this user and all others (excluding self)
        similar_users = self.similarity_df[user_id].drop(user_id).sort_values(ascending=False)

        #Get the ratings of the most similar users
        similar_users_ratings = self.user_matrix.loc[similar_users.index]

        #Compute weighted ratings: dot product of similar users' ratings and similarity scores
        weighted_ratings = similar_users_ratings.T.dot(similar_users)

        #Normalize the scores by the sum of similarity weights
        weighted_ratings /= similar_users.sum()

        #Identify which movies the user has not yet rated
        seen_movies = self.user_matrix.loc[user_id]
        unseen = seen_movies[seen_movies == 0].index

        #Return None if user has already rated all movies
        if len(unseen) == 0:
            return None

        #Select top-N highest scoring unseen movies
        recommendations = weighted_ratings[unseen].sort_values(ascending=False).head(top_n)

        return recommendations