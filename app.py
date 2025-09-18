import streamlit as st
import pickle
import pandas as pd
def recommand(selected_movie):
    movie_index=movies[movies['title']==selected_movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movie=[]
    for i in movie_list:
        movie_id=i[0]
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommended System')
selected_movie_name=st.selectbox('Search. Discover. Watch',movies['title'].values)
if st.button('Recommend'):
    recommendations=recommand(selected_movie_name)
    for i in recommendations:
        st.write(i)