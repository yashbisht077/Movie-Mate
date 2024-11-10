import pandas as pd
import numpy as np
import streamlit as st
import requests
import pickle
import time

# Movie Recommender System using Streamlit
# About Me

# Hi! I’m Shankar Singh, a second-year B.Tech student pursuing Computer Science and Engineering (CSE). During my second year, I developed MovieMate, a movie recommendation app, which allowed me to explore my interests in data science, machine learning, and web development.
# The MovieMate app uses a content-based recommendation system to provide personalized movie suggestions based on user preferences. The app fetches movie data from The Movie Database API and leverages algorithms to recommend similar movies, making it a practical application of machine learning in real-world scenarios.
# I am passionate about expanding my knowledge of technology, and I enjoy working on projects that integrate data structures, algorithms, and machine learning. Feel free to explore my repository, and reach out if you want to collaborate or discuss ideas!
# Let me know if you’d like to add anything else!

# This application provides movie recommendations based on a selected movie from a predefined list.
# It uses a content-based recommendation algorithm with similarity metrics stored in a pickle file.
# Users can select how many movies they want to be recommended and optionally apply a rating filter.
# If the filter is enabled, only movies with a rating above the user-defined threshold will be recommended.
# The movie posters and average ratings are fetched from an external API (The Movie Database API).
# Key functions:
# - fetch_movie_details: Fetches movie poster URL and rating from The Movie Database API.
# - get_movie_recommendations: Provides a list of movie recommendations based on similarity scores.
# - get_filtered_recommendations: Provides a list of movie recommendations filtered by the user-defined rating threshold.
# The Streamlit interface allows users to select a movie, set a number of recommended movies, and toggle the rating filter.
# The recommended movies, their posters, and ratings are displayed on the app's interface.

# API Keys for Movie Database
api_keys = [
    "58d20f63752ade8c6e45e49c08002a38",
    "8265bd1679663a7ea12ac168da84d2e8",
    "53070df475a34d2304aded57801fde38",
    "36107e2c5e86005819066f1aec8dca34",
    "27ce69086ff30b91cc60c0a4f465c5d"
]

# Function to fetch movie poster and rating based on movie_id
def fetch_movie_details(movie_id):
    url_template = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US"

    for api_key in api_keys:
        url = url_template.format(movie_id, api_key)

        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()

                poster_path = data.get('poster_path')
                vote_average = data.get('vote_average', 'N/A')

                poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else "https://via.placeholder.com/500"

                return poster_url, vote_average

        except requests.exceptions.RequestException:
            continue

    return "https://via.placeholder.com/500", "N/A"

# Load similarity data from pickle file
similarity_matrix = pickle.load(open("models/similarity.pkl", "rb"))

# Function to recommend movies based on similarity
def get_movie_recommendations(movie, num_recommendations):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity_matrix[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    recommended_movie_posters = []
    for i in distances[1:num_recommendations+1]:
        movie_id = movie_list.at[i[0], 'movie_id']
        poster_url, vote_average = fetch_movie_details(movie_id)
        recommended_movie_posters.append((poster_url, vote_average))
        recommended_movies.append(movie_list.iloc[i[0]].title)
    return recommended_movies, recommended_movie_posters

# Function to recommend movies with rating filter
def get_filtered_recommendations(movie, num_recommendations, min_rating):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity_matrix[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    recommended_movie_posters = []
    for i in distances[1:]:
        movie_index = i[0]
        similarity_score = i[1]
        vote_average = movie_list.iloc[movie_index]['vote_average']
        if vote_average >= min_rating:
            movie_id = movie_list.at[i[0], 'movie_id']
            poster_url, vote_average = fetch_movie_details(movie_id)
            recommended_movie_posters.append((poster_url, vote_average))
            recommended_movies.append(movie_list.iloc[i[0]].title)
            if len(recommended_movies) == num_recommendations:
                break
    return recommended_movies, recommended_movie_posters

# Streamlit user interface setup
st.title("_Movie-:blue[Mate]_ :movie_camera:")

# Load movie list data from pickle file
movie_list = pickle.load(open("models/movie_list.pkl", "rb"))
NumberOfMovieList = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Movie selection dropdown
selected_movie = st.selectbox(
    "Select a Movie",
    movie_list["title"]
)

# Number of movies to recommend dropdown
num_movies_to_recommend = st.selectbox(
    "How Many Movies to Recommend",
    NumberOfMovieList
)

# Rating filter toggle and rating selection
if "filter_enabled" not in st.session_state:
    st.session_state.filter_enabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox(
        "Would you like to turn on or off the filter for ratings above a certain threshold?",
        key="filter_enabled"
    )
with col2:
    rating_threshold = st.selectbox(
        "Minimum Rating?",
        options=[float(x) for x in range(1, 11)],
        disabled=not st.session_state.filter_enabled
    )

# Show recommendations on button click
if st.button("Show Recommendation"):
    if st.session_state.filter_enabled:
        recommended_movie_names, recommended_movie_posters = get_filtered_recommendations(selected_movie, num_movies_to_recommend, rating_threshold)
    else:
        recommended_movie_names, recommended_movie_posters = get_movie_recommendations(selected_movie, num_movies_to_recommend)

    cols = st.columns(num_movies_to_recommend)
    for i in range(num_movies_to_recommend):
        with cols[i]:
            st.text(recommended_movie_names[i])
            poster_url, vote_average = recommended_movie_posters[i]
            st.markdown(f"Rating:star:: {vote_average}")
            st.image(poster_url)
