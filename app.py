import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies_list[movies_list == movie].index[0]
    distances = similarity[movie_index]
    # sort the distance in the reverse manner
    rec_movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie = []
    for i in rec_movies_list:
        recommended_movie.append(movies_list.iloc[i[0]].title)
    return recommended_movie

st.title('Movie Recommendor System')
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list = pd.DataFrame(movies_list, columns=['title'])  # Convert to DataFrame

similarity = pickle.load(open('similarity.pkl', 'rb'))
selected_movie_name = st.selectbox(
    'Select the movie',
    movies_list['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
