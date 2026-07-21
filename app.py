import streamlit as st
import pickle
import requests
import time
import os

def fetch(movie_id, api_key):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    for attempt in range(3):
        try:
            response = requests.get(url, verify=False, timeout=20)
            response.raise_for_status()
            data = response.json()

            if data.get("poster_path"):
                return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

        except requests.exceptions.RequestException:
            if attempt < 2:
                time.sleep(2)

    return "https://via.placeholder.com/500x750?text=Poster+Unavailable"

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_posters=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch(movies.iloc[i[0]].movie_id, api_key))
    return recommended_movies, recommended_posters

st.title("Movie Recommender System")
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
api_key = os.getenv("TMDB_API_KEY")
if not api_key:
    st.error("TMDB_API_KEY environment variable is required.")
    st.stop()

selected_movie = st.selectbox(
    'Select a movie from the list below:',
    movies['title'].values
)
if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    