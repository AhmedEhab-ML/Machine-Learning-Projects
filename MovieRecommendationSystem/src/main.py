import random
from data_loader import DataLoader
from similarity import SimilarityCalculator
from recommender import Recommender
from evaluation import Evaluator

def main():
    # Ask user for filtering method
    print("Select filtering method:")
    print("1. User-based Collaborative Filtering")
    print("2. Item-based Collaborative Filtering")
    method_input = input("Enter 1 or 2: ").strip()
    if method_input == "1":
        method = 'user'
    elif method_input == "2":
        method = 'item'
    else:
        print("Invalid input. Exiting.")
        return

    # Load data
    data_loader = DataLoader(data_dir="../data")
    ratings, users, movies = data_loader.load_data()
    train_data, test_data = data_loader.load_train_test()

    sim_calc = SimilarityCalculator(train_data)

    if method == 'user':
        train_matrix = sim_calc.create_user_item_matrix()
        similarity_df = sim_calc.compute_user_similarity(train_matrix)
        recommender = Recommender(train_matrix, similarity_df)
        eval_func = lambda user_id, top_n=5: recommender.recommend_movies(user_id, top_n, method='user')
    else:
        item_user_matrix = sim_calc.create_item_user_matrix()
        item_similarity_df = sim_calc.compute_item_similarity(item_user_matrix)
        # For item-based, we still need user_matrix and user_similarity_df for the constructor, but only item matrices will be used
        user_matrix = sim_calc.create_user_item_matrix()
        user_similarity_df = sim_calc.compute_user_similarity(user_matrix)
        recommender = Recommender(user_matrix, user_similarity_df, item_user_matrix, item_similarity_df)
        eval_func = lambda user_id, top_n=5: recommender.recommend_movies(user_id, top_n, method='item')

    evaluator = Evaluator(eval_func, train_data, None, test_data, movies)

    # Evaluate on random users
    test_users = test_data['user_id'].unique()
    num_users = min(5, len(test_users))
    random_users = random.sample(list(test_users), num_users)

    precisions = []
    for uid in random_users:
        score = evaluator.precision_at_k(uid, k=5)
        if score is not None:
            precisions.append(score)
    if precisions:
        print("Average Precision@5:", sum(precisions) / len(precisions))
    else:
        print("No valid users found for evaluation.")

if __name__ == "__main__":
    main()