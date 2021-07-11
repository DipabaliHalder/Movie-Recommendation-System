import streamlit as st
import pickle
import numpy as np
import requests

def fetch_poster(movie,year):
    url = "https://www.omdbapi.com/?apikey=21dcff44&t={0}&y={1}".format(movie,year)
    data = requests.get(url)
    data = data.json()
    if(data['Response']=='True'):
        return data['Poster']
    else:
        return ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSS_amboXup4y-90QzAhgy8Q_7ZUwTsa-l6Bx11g3dPUz54vtAbwi5SbcFPFVbx6fE8Jig&usqp=CAU")


def recommend(movie):
    index = movies[movies['movie_name'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names=[]
    recommended_movie_posters=[]
    for i in distances[1:6]:
        m=movies.iloc[i[0]].movie_name
        y=movies.iloc[i[0]].year
        recommended_movie_names.append(m)
        recommended_movie_posters.append(fetch_poster(m,y))
    return recommended_movie_names,recommended_movie_posters

st.header("**Movie Recommender System**")

movies=pickle.load(open('finalmovie_list.pkl','rb'))
similarity= pickle.load(open('finalsimilarity.pkl','rb'))

movie_list = movies['movie_name'].unique()
movie_list=np.insert(movie_list,0,'')
selected_movie = st.selectbox("Choose a Movie: ",movie_list)

if st.button("Recommend >>"):
    if (selected_movie ==''):
        st.subheader("*No movie selected!!! Please select a movie.*")
    else:
        recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
        col1, col2, col3, col4, col5 = st.beta_columns(5)
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])
        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])
