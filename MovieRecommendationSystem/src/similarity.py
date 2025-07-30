import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class SimilarityCalculator:
    def __init__(self, train_data):
        """
        Initialize the SimilarityCalculator with training data.

        Parameters:
        train_data (DataFrame): Dataset containing user_id, movie_id, and rating columns.
        """
        self.train_data = train_data

    def create_user_item_matrix(self):
        """
        Create a user-item matrix from the training data.

        Returns:
        user_item_matrix (DataFrame): A matrix where rows represent users, columns represent movies,
                                      and values represent ratings. Missing ratings are filled with 0.
        """
        # Convert the train_data into a user-item matrix (rows: users, columns: movies)
        matrix = self.train_data.pivot_table(index='user_id', columns='movie_id', values='rating')
        return matrix.fillna(0)  # Fill missing ratings with 0 for similarity calculation

    def compute_user_similarity(self, user_matrix):
        """
        Compute the pairwise cosine similarity between users based on the user-item matrix.

        Parameters:
        user_matrix (DataFrame): The user-item matrix where each row is a user and each column is a movie.

        Returns:
        similarity_df (DataFrame): DataFrame representing cosine similarity between all user pairs.
                                   Rows and columns are indexed by user_id.
        """
        # Compute cosine similarity between all user vectors
        sim = cosine_similarity(user_matrix)

        # Return as a DataFrame with user_id indices and columns
        return pd.DataFrame(sim, index=user_matrix.index, columns=user_matrix.index)
