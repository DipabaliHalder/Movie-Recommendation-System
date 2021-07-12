import streamlit as st
import pickle
import numpy as np
import requests

def fetch_poster(movie):
    url = "https://www.omdbapi.com/?apikey=21dcff44&t={}".format(movie)
    data = requests.get(url)
    data = data.json()
    try:
        return data['Poster']
    except:
        return ('')


def recommend(movie):
    index = movies[movies['movie_name'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names=[]
    recommended_movie_posters=[]
    for i in distances[1:6]:
        m=movies.iloc[i[0]].movie_name
        recommended_movie_names.append(m)
        recommended_movie_posters.append(fetch_poster(m))
    return recommended_movie_names,recommended_movie_posters

st.header("**Movie Recommender System**")


movies=pickle.load(open('finalmovie_list.pkl','rb'))
similarity= pickle.load(open('finalsimilarity.pkl','rb'))

movie_list = np.sort(movies['movie_name'].unique())
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
            if(recommended_movie_posters[0]!=''):
                st.image(recommended_movie_posters[0])
            else:
                st.image("http://www.movienewz.com/img/films/poster-holder.jpg")
        with col2:
            st.text(recommended_movie_names[1])
            if (recommended_movie_posters[1]!= ''):
                st.image(recommended_movie_posters[1])
            else:
                st.image("http://www.movienewz.com/img/films/poster-holder.jpg")
        with col3:
            st.text(recommended_movie_names[2])
            if (recommended_movie_posters[2] != ''):
                st.image(recommended_movie_posters[2])
            else:
                st.image("http://www.movienewz.com/img/films/poster-holder.jpg")
        with col4:
            st.text(recommended_movie_names[3])
            if (recommended_movie_posters[3] != ''):
                st.image(recommended_movie_posters[3])
            else:
                st.image("http://www.movienewz.com/img/films/poster-holder.jpg")
        with col5:
            st.text(recommended_movie_names[4])
            if (recommended_movie_posters[4] != ''):
                st.image(recommended_movie_posters[4])
            else:
                st.image("http://www.movienewz.com/img/films/poster-holder.jpg")
