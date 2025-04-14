import streamlit as st 
import pickle
import pandas as pd

book_dict=pickle.load(open(r'/Users/puravdoshi/Downloads/BookRecommenderSystem/popular.pkl','rb'))
similarity=pickle.load(open(r'/Users/puravdoshi/Downloads/BookRecommenderSystem/similarity.pkl','rb'))
books=pd.DataFrame(book_dict)

if not isinstance(similarity, pd.DataFrame):
    similarity = pd.DataFrame(similarity)
similarity = similarity.apply(pd.to_numeric, errors='coerce').fillna(0)

def recommend(book):
    index = books[books['Book-Title'] == book].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_book_names = []
    recommended_book_posters = []
    for i in distances:
        book_index = i[0]
        recommended_book_names.append(books.iloc[book_index]['Book-Title'])
        recommended_book_posters.append(books.iloc[book_index]['Image-URL-L'])
    return recommended_book_names, recommended_book_posters

st.title('Book Recommender System')

option=st.selectbox("What book do you want to read?", books['Book-Title'].values)

if(st.button("Recommend")):
    recommended_book_names, recommended_book_posters=recommend(option)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(recommended_book_posters[i])
            st.text(recommended_book_names[i])
