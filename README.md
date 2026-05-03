# 🎬 Netflix Movie Recommender

A Netflix-style movie recommendation system built using Machine Learning and deployed as an interactive web app.

## 🚀 Live Demo

👉 https://netflix-movie-recommender-dczmc7jegbqyberlqrkzua.streamlit.app/

## ✨ Features
🎯 Content-based movie recommendation system
🎬 Supports Hollywood + Bollywood movies
⭐ Displays IMDB ratings and release year
🖼 Fetches real-time posters using OMDB API
🎨 Netflix-inspired UI with hover animations
⚡ Fast and interactive Streamlit interface
🌐 Fully deployed on Streamlit Cloud
🧠 How It Works
Movie data is processed into textual features (genres, keywords, etc.)
TF-IDF Vectorization converts text into numerical vectors
Cosine Similarity finds movies with similar content
Recommendations are filtered based on industry (Bollywood/Hollywood)

## 🛠 Tech Stack
Python
Pandas
Scikit-learn
Streamlit
OMDB API
gdown (for dataset download)

## 📦 Dataset Handling

Due to GitHub’s file size limits, large files are not stored directly in the repository.

Instead:

movies.pkl and similarity.pkl are hosted on Google Drive
They are automatically downloaded at runtime using gdown

So users do NOT need to manually download anything ✅

## 🔐 API Setup (Important)

This app uses the OMDB API for movie posters and ratings.

For local run:

Create a .streamlit/secrets.toml file:

API_KEY = "your_omdb_api_key"
For deployment:

Add the API key in Streamlit Cloud → Settings → Secrets

👉 Your API key is not exposed publicly (secure)

## ⚙️ Run Locally
git clone https://github.com/YOUR_USERNAME/netflix-movie-recommender.git
cd netflix-movie-recommender
pip install -r requirements.txt
streamlit run app.py

## 📸 Screenshots
<img width="1502" height="858" alt="Screenshot 2026-05-03 at 20 07 35" src="https://github.com/user-attachments/assets/6fd1787f-9f70-406b-8c67-7886bee5445d" />


## 💡 Future Improvements
🔍 Search-based recommendations
🎭 Genre filtering
📊 Explainable recommendations
❤️ User-based personalization

## 🙌 By
Manisha Singh

⭐ If you like this project
Give it a ⭐ on GitHub!
