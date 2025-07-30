from flask import Flask, render_template, request
import random
from data_loader import DataLoader
from similarity import SimilarityCalculator
from recommender import Recommender
from evaluation import Evaluator

app = Flask(__name__)

# Load and prepare everything once
data_loader = DataLoader(data_dir="../data")
ratings, users, movies = data_loader.load_data()
train_data, test_data = data_loader.load_train_test()
sim_calc = SimilarityCalculator(train_data)
user_item_matrix = sim_calc.create_user_item_matrix()
user_similarity_df = sim_calc.compute_user_similarity(user_item_matrix)
item_user_matrix = sim_calc.create_item_user_matrix()
item_similarity_df = sim_calc.compute_item_similarity(item_user_matrix)
recommender = Recommender(user_item_matrix, user_similarity_df, item_user_matrix, item_similarity_df)
evaluator = Evaluator(recommender.recommend_movies, user_item_matrix, user_similarity_df, test_data, movies)

@app.route('/', methods=['GET', 'POST'])
def index():
    details = None
    selected_method = 'user'
    if request.method == 'POST':
        if request.form.get('clear'):
            return render_template('index.html', details=None, selected_method='user')
        user_id = request.form.get('user_id')
        top_n = request.form.get('top_n', 5)
        selected_method = request.form.get('method', 'user')
        try:
            user_id = int(user_id)
            top_n = int(top_n)
            if top_n < 1:
                details = {"error": "Number of recommendations must be at least 1."}
            elif user_id not in test_data['user_id'].values:
                details = {"error": f"User ID {user_id} is not found in the database."}
            else:
                recs = recommender.recommend_movies(user_id, top_n=top_n, method=selected_method)
                movie_id_to_title = dict(zip(movies['movie_id'], movies['title']))
                rec_titles = [movie_id_to_title.get(mid, f"Movie {mid}") for mid in recs.index] if recs is not None else []
                user_test_data = test_data[test_data['user_id'] == user_id]
                relevant = set(user_test_data[user_test_data['rating'] >= 4]['movie_id'])
                relevant_titles = [movie_id_to_title.get(mid, f"Movie {mid}") for mid in relevant]
                hits = [1 for movie_id in recs.index if movie_id in relevant] if recs is not None else []
                num_hits = sum(hits)
                precision = num_hits / top_n if top_n > 0 else 0.0
                details = {
                    "rec_titles": rec_titles,
                    "relevant_titles": relevant_titles,
                    "num_hits": num_hits,
                    "precision": f"{precision:.3f}",
                    "top_n": top_n,
                    "user_id": user_id,
                    "method": selected_method
                }
        except Exception as e:
            details = {"error": "Invalid input. Please enter valid numbers."}
    return render_template('index.html', details=details, selected_method=selected_method)

if __name__ == '__main__':
    app.run(debug=True)