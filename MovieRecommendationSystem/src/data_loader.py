import pandas as pd

class DataLoader:
    def __init__(self, data_dir="../data"):
        """
        Initialize the DataLoader with the directory path where the dataset files are located.

        Parameters:
        data_dir (str): Path to the directory containing the data files. Defaults to "../data".
        """
        self.data_dir = data_dir

    def load_data(self):
        """
        Load the full MovieLens dataset including ratings, user information, and movie metadata.

        Returns:
        ratings (DataFrame): DataFrame containing user-movie ratings.
        users (DataFrame): DataFrame containing user demographic information.
        movies (DataFrame): DataFrame containing movie metadata and genre information.
        """
        ratings = pd.read_csv(f"{self.data_dir}/u.data", sep="\t",
                              names=["user_id", "movie_id", "rating", "timestamp"])

        users = pd.read_csv(f"{self.data_dir}/u.user", sep="|",
                            names=["user_id", "age", "gender", "occupation", "zip_code"])

        movies = pd.read_csv(f"{self.data_dir}/u.item", sep="|", encoding='latin-1', header=None,
                             names=["movie_id", "title", "release_date", "video_release_date", "IMDb_URL"] +
                                   [f"genre_{i}" for i in range(19)], usecols=range(24))

        return ratings, users, movies

    def load_train_test(self):
        """
        Load the training and test datasets used for model evaluation (typically u1.base and u1.test).

        Returns:
        train (DataFrame): Training data with columns [user_id, movie_id, rating].
        test (DataFrame): Test data with columns [user_id, movie_id, rating].
        """
        train = pd.read_csv(f"{self.data_dir}/u1.base", sep="\t",
                            names=["user_id", "movie_id", "rating", "timestamp"])
        test = pd.read_csv(f"{self.data_dir}/u1.test", sep="\t",
                           names=["user_id", "movie_id", "rating", "timestamp"])

        train.drop('timestamp', axis=1, inplace=True)
        test.drop('timestamp', axis=1, inplace=True)

        return train, test