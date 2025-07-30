# Movie Recommendation System

<img width="942" height="601" alt="homepage" src="https://github.com/user-attachments/assets/74dac534-c2a3-4470-ab35-c4c058ff2db8" />

## Overview

This project is a **Movie Recommendation System** built with Python and Flask. It demonstrates how collaborative filtering (both user-based and item-based) can be used to recommend movies to users based on their preferences. The application features a professional web interface where users can input their user ID, select the filtering method, and receive personalized movie recommendations along with relevant statistics.

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
│   ├── similarity.py    # Computes user and item similarity matrices
│   ├── recommender.py   # Generates movie recommendations (user-based & item-based)
│   ├── evaluation.py    # Evaluates recommendation quality
│   └── templates/
│       └── index.html   # Web UI template
├── movie_recommendation_system.ipynb # Jupyter notebook for prototyping and data analysis
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

## Features & How It Works

1. **Data Loading**  
   The `DataLoader` class loads and splits the data into training and test sets.

2. **Similarity Calculation**  
   The `SimilarityCalculator` class creates both user-item and item-user matrices, and computes user-user and item-item similarity matrices using cosine similarity.

3. **Recommendation Generation**  
   The `Recommender` class supports both user-based and item-based collaborative filtering.  
   - **User-based**: Recommends movies based on similar users' preferences.
   - **Item-based**: Recommends movies based on similarity between items (movies) the user has already rated.

4. **Evaluation**  
   The `Evaluator` class computes metrics like Precision@K to assess recommendation quality for both filtering types.

5. **Web Application**  
   The Flask app (`app.py`) provides a user-friendly interface:
   - Enter a user ID and number of recommendations.
   - Select the filtering type: **User-based** or **Item-based**.
   - View top recommended movies, relevant movies (liked by the user), hit count, and precision.
   - Use the "Clear" button to reset the results.

6. **Jupyter Notebook**  
   The project includes a notebook (`movie_recommendation_system.ipynb`) used for prototyping, exploratory data analysis, and testing recommendation logic before integrating into the main application.

---

## Application Usage

### 1. **Setup**

- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
  Or, if you don't have a `requirements.txt` file, install manually:
  ```bash
  pip install flask pandas numpy scikit-learn
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
- Select the filtering type (**User-based** or **Item-based**).
- Click **Get Recommendations** to view results.
- Click **Clear** to reset the output and start a new

---

<img width="1351" height="917" alt="results" src="https://github.com/user-attachments/assets/f17e5d7d-be95-437f-9820-9252183e9301" />

---

## File Descriptions

- **app.py**  
  The main Flask application. Handles user input, generates recommendations (user-based or item-based), and renders the UI.

- **main.py**  
  Script for batch evaluation of recommendation quality (Precision@K) across multiple users. Prompts the user to select the filtering method before execution.

- **data_loader.py**  
  Loads ratings, users, and movies data. Splits data into training and test sets.

- **similarity.py**  
  Computes both user-item and item-user matrices, as well as user-user and item-item similarity matrices.

- **recommender.py**  
  Contains logic for generating movie recommendations for a user using either user-based or item-based collaborative filtering.

- **evaluation.py**  
  Provides evaluation metrics (e.g., Precision@K) for recommendations.

- **templates/index.html**  
  The web interface template. Styled for a professional look and user experience. Now supports selecting the filtering type.

- **movie_recommendation_system.ipynb**  
  Jupyter notebook used for prototyping, exploratory data analysis, and testing recommendation logic.

---

## Example Workflow

1. **User enters their User ID and desired number of recommendations.**
2. **User selects the filtering type (User-based or Item-based).**
3. **System computes recommendations using the selected collaborative filtering method.**
4. **Results are displayed:**
   - Top N recommended movies (by title)
   - Relevant movies the user liked (rated ≥ 4)
   - Number of hits (correct recommendations)
   - Precision@N score
5. **User can clear results and start a new query.**

---

## Customization

- You can adjust the recommendation logic in `recommender.py` (e.g., change similarity metric or weighting).
- You can modify the UI in `templates/index.html` for branding or additional features.
- The evaluation logic in `evaluation.py` can be extended for more metrics.
- The notebook (`movie_recommendation_system.ipynb`) can be used for further prototyping and analysis.

---

## License

This project is provided for educational purposes. Please check the data source licenses before using in production.

---

## Author

Developed by [Ahmed Ehab].  
Feel free to contribute or open issues on GitHub!
