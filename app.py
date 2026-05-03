import streamlit as st
import pickle
import requests
import base64


st.set_page_config(layout="wide")


API_KEY = st.secrets["API_KEY"]


import os
import requests

def download_file(url, filename):
    if not os.path.exists(filename):
        r = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(r.content)

movies_url = "https://drive.google.com/uc?id=1Sdq6Fk-neGcXCpdNJ66TMg18aH2yOEni"
similarity_url = "https://drive.google.com/uc?id=1uSwY3uTOEIm_WtgknPIvpwABJV-bR2Qm"

download_file(movies_url, "movies.pkl")
download_file(similarity_url, "similarity.pkl")

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


def get_base64_image(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = get_base64_image("bg.jpg")


st.markdown(f"""
<style>

[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{bg_img}");
    background-size: cover;
    background-position: center;
}}

[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.7);
}}

[data-testid="stAppViewContainer"] > div {{
    position: relative;
    z-index: 1;
}}

img {{
    border-radius: 12px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}}

img:hover {{
    transform: scale(1.08);
    box-shadow: 0 10px 30px rgba(229,9,20,0.6);
}}

</style>
""", unsafe_allow_html=True)

# FETCH MOVIE DATA 
def fetch_movie_data(title):
    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
        data = requests.get(url).json()

        poster = data.get("Poster") if data.get("Poster") != "N/A" else "https://via.placeholder.com/300x450?text=No+Image"
        rating = data.get("imdbRating", "N/A")
        year = data.get("Year", "N/A")

        return poster, rating, year
    except:
        return "https://via.placeholder.com/300x450?text=No+Image", "N/A", "N/A"

# RECOMMEND
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    selected_industry = movies.iloc[index]['industry']

    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    names = []

    for i in movie_list:
        m = movies.iloc[i[0]]
        if m['industry'] == selected_industry and m['title'] != movie:
            names.append(m['title'])
        if len(names) == 5:
            break

    return names

#UI

st.markdown("""
<h1 style='text-align: center; color: #e50914; font-size: 50px;'>
🎬 Netflix Recommender
</h1>
<p style='text-align: center; color: gray; font-size: 16px;'>
Discover movies you'll love 🍿
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

selected_movie = st.selectbox("Choose a movie", movies['title'].values)

if st.button("Recommend"):
    names = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            poster, rating, year = fetch_movie_data(names[i])

            st.image(poster)
            st.markdown(f"**{names[i]}**")
            st.markdown(f"⭐ {rating} | 📅 {year}")