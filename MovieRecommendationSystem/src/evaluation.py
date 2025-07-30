class Evaluator:
    def __init__(self, recommend_func, train_matrix, similarity_df, test_data, movies_data):
        """
        Initialize the Evaluator with required data and recommendation function.

        Parameters:
        recommend_func (function): Function that takes a user_id and returns recommended movie IDs.
        train_matrix (DataFrame): User-item matrix from the training set.
        similarity_df (DataFrame): Item-item similarity matrix.
        test_data (DataFrame): Test dataset containing user_id, movie_id, and rating.
        movies_data (DataFrame): Dataset containing movie metadata including movie_id and title.
        """
        self.recommend_func = recommend_func
        self.train_matrix = train_matrix
        self.similarity_df = similarity_df
        self.test_data = test_data
        self.movies_data = movies_data

        # Map movie_id to movie title for display purposes
        self.movie_id_to_title = dict(zip(movies_data['movie_id'], movies_data['title']))

    def precision_at_k(self, user_id, k=5):
        """
        Compute Precision@k for a given user.

        Precision@k measures the proportion of the top-k recommended items that are relevant.

        Parameters:
        user_id (int): ID of the user to evaluate.
        k (int): Number of top recommendations to consider. Default is 5.

        Returns:
        precision (float or None): Precision@k value for the user, or None if user not found or no recommendations.
        """
        # Check if the user exists in the test set
        if user_id not in self.test_data['user_id'].values:
            print(f"User ID {user_id} not found in test data.")
            return None

        #Get top-k recommendations for the user
        recs = self.recommend_func(user_id, top_n=k)
        if recs is None or len(recs) == 0:
            print(f"No recommendations found for User ID {user_id}.")
            return None

        #Convert recommended movie IDs to titles for better interpretability
        rec_titles = [self.movie_id_to_title.get(mid, f"Movie {mid}") for mid in recs.index]

        #Filter relevant movies for the user in the test data (ratings ≥ 4)
        user_test_data = self.test_data[self.test_data['user_id'] == user_id]
        relevant = set(user_test_data[user_test_data['rating'] >= 4]['movie_id'])
        relevant_titles = [self.movie_id_to_title.get(mid, f"Movie {mid}") for mid in relevant]

        #Count how many recommended movies are relevant
        hits = [1 for movie_id in recs.index if movie_id in relevant]
        num_hits = sum(hits)

        #Calculate precision
        precision = num_hits / k

        #Display evaluation details
        print(f"\n🎯 Precision@{k} for User ID {user_id}:")
        print(f"- 🧠 Top {k} Recommended Movies: {rec_titles}")
        print(f"- ✅ Relevant Movies (rated ≥ 4): {relevant_titles}")
        print(f"- ✔️ Hits (Correct Recommendations): {num_hits}")
        print(f"- 📊 Precision@{k} = {num_hits} / {k} = {precision:.3f}")

        return precision
