import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
  movie_index=movies[movies['title']==movie].index[0]
  distances=similarity[movie_index]
  movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  reco=[]
  for i in movies_list:
    reco.append(movies.iloc[i[0]].title)
  return reco
similarity=pickle.load(open('similarity.pkl','rb'))
movies_list=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_list)
st.title('Movie Recommender System')
option=st.selectbox('how',movies['title'].values)
if st.button('Recommend'):
    recommendations=recommend(option)
    for i in recommendations:
       st.write(i)