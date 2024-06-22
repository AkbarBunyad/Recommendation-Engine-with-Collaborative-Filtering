import pickle
import streamlit as st
import numpy as np

st.header('Book Recommendation System')
model = pickle.load(open('artifacts/model.pkl', 'rb'))
book_names = pickle.load(open('artifacts/book_names.pkl', 'rb'))
final_ratings = pickle.load(open('artifacts/final_ratings.pkl', 'rb'))
pivot = pickle.load(open('artifacts/pivot.pkl', 'rb'))

selected_book = st.selectbox(
    "Type or select a book",
    book_names
)

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(pivot.index[book_id])
    
    for name in book_name[0]:
        ids = np.where(final_ratings['title'] == name)[0][0]
        ids_index.append(ids)
    
    for idx in ids_index:
        url = final_ratings.iloc[idx]['img_url']
        poster_url.append(url)
    
    return poster_url

def recommender(book_name):
    lst = []
    book_id = np.where(pivot.index == book_name)[0][0]
    distance, index = model.kneighbors(pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors = 6)
    poster_url = fetch_poster(index)
    for i in range(0, index.shape[1]):
        if i!=0:
            lst.append(pivot.index[index[0, i]])
    
    return lst, poster_url

if st.button("Show Recommendation"):
    books, poster_url = recommender(selected_book)
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.text(books[0])
        st.image(poster_url[0])
    
    with c2:
        st.text(books[1])
        st.image(poster_url[1])
    
    with c3:
        st.text(books[2])
        st.image(poster_url[2])
    
    with c4:
        st.text(books[3])
        st.image(poster_url[3])
    
    with c5:
        st.text(books[4])
        st.image(poster_url[4])