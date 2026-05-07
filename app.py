import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load your data (we will save it first)
new_df = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    if movie not in new_df['title'].values:
        return ["Movie not found"]
    
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended = []
    for i in movie_list:
        recommended.append(new_df.iloc[i[0]].title)
    
    return recommended

st.title("🎬 Movie Recommendation System")

movie_name = st.text_input("Enter a movie name")

if st.button("Recommend"):
    recommendations = recommend(movie_name)
    
    for movie in recommendations:
        st.write(movie)