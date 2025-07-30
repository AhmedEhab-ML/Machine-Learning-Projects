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
        user_item_matrix (DataFrame): Rows are users, columns are movies, values are ratings (0 if missing).
        """
        matrix = self.train_data.pivot_table(index='user_id', columns='movie_id', values='rating')
        return matrix.fillna(0)
    
    def create_item_user_matrix(self):
        """
        Create an item-user matrix from the training data.

        Returns:
        item_user_matrix (DataFrame): Rows are movies, columns are users, values are ratings (0 if missing).
        """
        return self.train_data.pivot_table(index='movie_id', columns='user_id', values='rating').fillna(0)

    def compute_user_similarity(self, user_matrix):
        """
        Compute the pairwise cosine similarity between users.

        Parameters:
        user_matrix (DataFrame): User-item matrix.

        Returns:
        similarity_df (DataFrame): Cosine similarity between all user pairs.
        """
        sim = cosine_similarity(user_matrix)
        return pd.DataFrame(sim, index=user_matrix.index, columns=user_matrix.index)
    
    def compute_item_similarity(self, item_user_matrix):
        """
        Compute the pairwise cosine similarity between items (movies).

        Parameters:
        item_user_matrix (DataFrame): Item-user matrix.

        Returns:
        similarity_df (DataFrame): Cosine similarity between all item pairs.
        """
        similarity = cosine_similarity(item_user_matrix)
        similarity_df = pd.DataFrame(similarity, index=item_user_matrix.index, columns=item_user_matrix.index)
        return similarity_df