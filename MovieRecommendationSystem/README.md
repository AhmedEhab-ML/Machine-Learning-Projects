# Movie Recommendation System

<img width="942" height="601" alt="homepage" src="https://github.com/user-attachments/assets/74dac534-c2a3-4470-ab35-c4c058ff2db8" />


## Overview

This project is a **Movie Recommendation System** built with Python and Flask. It demonstrates how collaborative filtering and user similarity can be used to recommend movies to users based on their preferences. The application features a professional web interface where users can input their user ID and receive personalized movie recommendations, along with relevant statistics.

---

## Project Structure

```
Movie Recommendation System/
│
├── data/                # Contains ratings, users, and movies data (CSV files)
├── src/
│   ├── app.py           # Flask web application
│   ├── main.py          # Script for running batch evaluations
│   ├── data_loader.py   # Loads and preprocesses the data
│   ├── similarity.py    # Computes user similarity matrix
│   ├── recommender.py   # Generates movie recommendations
│   ├── evaluation.py    # Evaluates recommendation quality
│   └── templates/
│       └── index.html   # Web UI template
└── README.md            # Project documentation
```

---

## Data

The system uses three main datasets (typically in CSV format):

- **ratings.csv**: Contains user ratings for movies (`user_id`, `movie_id`, `rating`).
- **users.csv**: Contains user information (`user_id`, ...).
- **movies.csv**: Contains movie information (`movie_id`, `title`, ...).

These files should be placed in the `data/` directory.

---

## How It Works

1. **Data Loading**  
   The `DataLoader` class loads and splits the data into training and test sets.

2. **User Similarity Calculation**  
   The `SimilarityCalculator` class creates a user-item matrix and computes user similarity (e.g., cosine similarity).

3. **Recommendation Generation**  
   The `Recommender` class uses the similarity matrix to recommend movies for a given user.

4. **Evaluation**  
   The `Evaluator` class computes metrics like Precision@K to assess recommendation quality.

5. **Web Application**  
   The Flask app (`app.py`) provides a user-friendly interface:
   - Enter a user ID and number of recommendations.
   - View top recommended movies, relevant movies (liked by the user), hit count, and precision.
   - Use the "Clear" button to reset the results.

---

## Application Usage

### 1. **Setup**

- Install dependencies:
  ```bash
  pip install flask pandas numpy
  ```
- Place your data files in the `data/` directory.

### 2. **Run the Web App**

```bash
cd src
python app.py
```

- Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

### 3. **Using the Interface**

- Enter a valid user ID and the number of top recommendations.
- Click **Get Recommendations** to view results.
- Click **Clear** to reset the output and start a new query.

---

<img width="1351" height="917" alt="results" src="https://github.com/user-attachments/assets/f17e5d7d-be95-437f-9820-9252183e9301" />


## File Descriptions

- **app.py**  
  The main Flask application. Handles user input, generates recommendations, and renders the UI.

- **main.py**  
  Script for batch evaluation of recommendation quality (Precision@K) across multiple users.

- **data_loader.py**  
  Loads ratings, users, and movies data. Splits data into training and test sets.

- **similarity.py**  
  Computes the user-item matrix and user similarity matrix.

- **recommender.py**  
  Contains logic for generating movie recommendations for a user.

- **evaluation.py**  
  Provides evaluation metrics (e.g., Precision@K) for recommendations.

- **templates/index.html**  
  The web interface template. Styled for a professional look and user experience.

---

## Example Workflow

1. **User enters their User ID and desired number of recommendations.**
2. **System computes recommendations using collaborative filtering.**
3. **Results are displayed:**
   - Top N recommended movies (by title)
   - Relevant movies the user liked (rated ≥ 4)
   - Number of hits (correct recommendations)
   - Precision@N score
4. **User can clear results and start a new query.**

---

## Customization

- You can adjust the recommendation logic in `recommender.py` (e.g., change similarity metric).
- You can modify the UI in `templates/index.html` for branding or additional features.
- The evaluation logic in `evaluation.py` can be extended for more metrics.

---

## License

This project is provided for educational purposes. Please check the data source licenses before using in production.

---

## Author

Developed by [Ahmed Ehab].  
Feel free to contribute or open issues on GitHub!
