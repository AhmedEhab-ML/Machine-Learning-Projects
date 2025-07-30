import pandas as pd

class Recommender:
    def __init__(self, user_matrix, user_similarity_df, item_user_matrix=None, item_similarity_df=None):
        """
        Initialize the Recommender with user-item ratings and similarity data.

        Parameters:
        user_matrix (DataFrame): User-item matrix (users as rows, movies as columns).
        user_similarity_df (DataFrame): User-user similarity matrix.
        item_user_matrix (DataFrame, optional): Item-user matrix (movies as rows, users as columns).
        item_similarity_df (DataFrame, optional): Item-item similarity matrix.
        """
        self.user_matrix = user_matrix
        self.user_similarity_df = user_similarity_df
        self.item_user_matrix = item_user_matrix
        self.item_similarity_df = item_similarity_df

    def recommend_movies(self, user_id, top_n=5, method='user'):
        """
        Generate top-N movie recommendations for a given user.

        Parameters:
        user_id (int): ID of the user to generate recommendations for.
        top_n (int): Number of top recommendations to return. Default is 5.
        method (str): 'user' for user-based, 'item' for item-based collaborative filtering.

        Returns:
        recommendations (Series or None): Series of recommended movie IDs with their weighted scores,
                                          or None if user not found or all movies are already seen.
        """
        if method == 'user':
            # User-based collaborative filtering
            if user_id not in self.user_matrix.index:
                return None
            similar_users = self.user_similarity_df[user_id].drop(user_id).sort_values(ascending=False)
            similar_users_ratings = self.user_matrix.loc[similar_users.index]
            weighted_ratings = similar_users_ratings.T.dot(similar_users)
            weighted_ratings /= similar_users.sum()
            seen_movies = self.user_matrix.loc[user_id]
            unseen = seen_movies[seen_movies == 0].index
            if len(unseen) == 0:
                return None
            recommendations = weighted_ratings[unseen].sort_values(ascending=False).head(top_n)
            return recommendations

        elif method == 'item':
            # Item-based collaborative filtering
            if self.item_user_matrix is None or self.item_similarity_df is None:
                raise ValueError("Item-user matrix and item similarity matrix must be provided for item-based filtering.")
            if user_id not in self.item_user_matrix.columns:
                return None
            user_ratings = self.item_user_matrix.loc[:, user_id]
            rated_movies = user_ratings[user_ratings > 0].index
            scores = pd.Series(0, index=self.item_user_matrix.index, dtype=float)
            for movie in rated_movies:
                sim_scores = self.item_similarity_df[movie]
                scores += sim_scores * user_ratings[movie]
            scores = scores.drop(rated_movies)
            if scores.empty:
                return None
            recommendations = scores.sort_values(ascending=False).head(top_n)
            return recommendations

        else:
            raise ValueError("Unknown method. Use 'user' or 'item'.")