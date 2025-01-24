import pandas as pd
import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=a6a3b4fb08b0819a607ddd5ccda4cfcd&language=en-US"
    response = requests.get(url)
    if response.status_code != 200:
        return "https://via.placeholder.com/500"  # Default image if API fails
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')


def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found! Please select a valid movie."], ["https://via.placeholder.com/500"]

    try:
        movie_index = movies[movies['title'] == movie].index[0]
    except IndexError:
        return ["Error: Movie not found in dataset!"], ["https://via.placeholder.com/500"]

    if movie_index >= len(similarity):
        return ["Error: Similarity matrix mismatch!"], ["https://via.placeholder.com/500"]

    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # Fixing DataFrame access
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


# Streamlit UI
st.title('Movie Recommendation System')
st.markdown("<br>", unsafe_allow_html=True)

with open('E:\MovieRecSystemMLProject\PycharmCode\movie_dict.pkl', 'rb') as file:
    movies_dict = pickle.load(file)

movies = pd.DataFrame(movies_dict)

with open('.venv/similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

selected_movie = st.selectbox(
    'Select a Movie to Get Recommendations: ',
    movies['title'].values
)

if st.button('Recommend'):
    st.markdown("<br>", unsafe_allow_html=True)
    names, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)  # Fixing st.beta_columns()

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
