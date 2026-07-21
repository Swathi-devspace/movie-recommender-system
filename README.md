# 🎬 Movie Recommendation System

A content-based movie recommendation system built using **Python**, **Scikit-learn**, and **Streamlit**. The application recommends movies based on their content by analyzing genres, cast, crew, keywords, and movie overviews using Natural Language Processing (NLP). Movie posters are fetched dynamically using the **TMDB API**.

## Live Demo

**Application:**  
https://movie-recommender-system-5p3nbew9h3ebqzvgqsuxwv.streamlit.app/

**GitHub Repository:**  
https://github.com/Swathi-devspace/movie-recommender-system

---

## Project Overview

Finding movies similar to a user's interests can be challenging with thousands of titles available. This project implements a **Content-Based Recommendation System** that suggests similar movies based on movie metadata instead of user ratings.

The recommendation engine converts textual movie information into numerical feature vectors using **CountVectorizer**, computes similarities using **Cosine Similarity**, and recommends the five most relevant movies. Movie posters are retrieved in real time through the TMDB API to provide a better user experience.

---

## Features

- Content-based movie recommendation
- Recommends top 5 similar movies
- Displays movie posters using TMDB API
- Interactive Streamlit web interface
- Fast recommendation using precomputed similarity matrix
- Secure API key management using Streamlit Secrets

---

## Application Preview

### Home Page

![Home Page](images/homepage.png)

### Recommendations

![Recommendations](images/recommendations.png)

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| NLP | CountVectorizer |
| Similarity Metric | Cosine Similarity |
| Frontend | Streamlit |
| API | TMDB API |
| Data Processing | Pandas, NumPy |
| Serialization | Pickle |

---

## Dataset

Dataset used:

- TMDB 5000 Movies Dataset
- TMDB 5000 Credits Dataset

The datasets contain movie metadata including:

- Title
- Genres
- Cast
- Crew
- Keywords
- Overview

These features are combined to build the recommendation engine.

---

## Recommendation Pipeline

```
TMDB Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Combine Important Features
      │
      ▼
Text Vectorization
(CountVectorizer)
      │
      ▼
Cosine Similarity Matrix
      │
      ▼
Store using Pickle
      │
      ▼
Streamlit Web Application
      │
      ▼
TMDB API
      │
      ▼
Movie Posters
```

---

## Project Structure

```
movie-recommender-system/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── images/
│   ├── homepage.png
│   └── recommendations.png
│
├── .streamlit/
│   └── secrets.toml
│
├── movies.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
└── movie-recommender-system.ipynb
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Swathi-devspace/movie-recommender-system.git
```

### 2. Navigate to the project directory

```bash
cd movie-recommender-system
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the TMDB API Key

Create the following file:

```
.streamlit/
└── secrets.toml
```

Add your TMDB API key:

```toml
TMDB_API_KEY="YOUR_API_KEY"
```

### 5. Run the application

```bash
streamlit run app.py
```

## How It Works

1. Load processed movie data.
2. Load the precomputed cosine similarity matrix.
3. User selects a movie.
4. Find the selected movie index.
5. Retrieve similarity scores.
6. Sort movies based on similarity.
7. Return the top five recommendations.
8. Fetch movie posters using the TMDB API.
9. Display movie titles and posters in the Streamlit application.

---

## Future Improvements

- Hybrid recommendation system
- Collaborative filtering
- Genre-based filtering
- Search by actor or director
- User authentication
- Personalized recommendations
- Movie trailers integration
- Rating and review system
- Cloud database integration
- Docker containerization

---

## Skills Demonstrated

- Machine Learning Fundamentals
- Natural Language Processing
- Feature Engineering
- Cosine Similarity
- Recommendation Systems
- API Integration
- Streamlit Deployment
- Data Preprocessing
- Python Programming
- Git & GitHub

---

## Acknowledgements

- TMDB for providing the movie metadata API.
- Streamlit for simplifying web application deployment.
- Scikit-learn for machine learning utilities.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
## Author

**Swathi Ponnaganti**

B.Tech – Artificial Intelligence and Machine Learning

GitHub: https://github.com/Swathi-devspace

LinkedIn: https://www.linkedin.com/in/swathi-p-32435b305?utm_source=share_via&utm_content=profile&utm_medium=member_android