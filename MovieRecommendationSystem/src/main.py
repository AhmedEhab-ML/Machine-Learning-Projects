import random
from data_loader import DataLoader
from similarity import SimilarityCalculator
from recommender import Recommender
from evaluation import Evaluator

def main():
    #Load data using DataLoader class
    data_loader = DataLoader(data_dir="../data")
    ratings, users, movies = data_loader.load_data()
    train_data, test_data = data_loader.load_train_test()

    #Create user-item matrix and similarity matrix using SimilarityCalculator class
    sim_calc = SimilarityCalculator(train_data)
    train_matrix = sim_calc.create_user_item_matrix()
    user_similarity_df = sim_calc.compute_user_similarity(train_matrix)

    #Create recommender and evaluator objects
    recommender = Recommender(train_matrix, user_similarity_df)
    evaluator = Evaluator(recommender.recommend_movies, train_matrix, user_similarity_df, test_data, movies)

    #Evaluate on random users
    test_users = test_data['user_id'].unique()

    num_users = min(10, len(test_users))
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