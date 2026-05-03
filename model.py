import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# HOLLYWOOD
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

movies = movies.merge(credits, on="title")
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]
movies.dropna(inplace=True)

def convert(obj):
    return [i['name'] for i in ast.literal_eval(obj)]

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

def convert_cast(obj):
    return [i['name'] for i in ast.literal_eval(obj)[:3]]

movies['cast'] = movies['cast'].apply(convert_cast)

def fetch_director(obj):
    return [i['name'] for i in ast.literal_eval(obj) if i['job'] == 'Director']

movies['crew'] = movies['crew'].apply(fetch_director)

def collapse(L):
    return [i.replace(" ", "") for i in L]

for col in ['genres','keywords','cast','crew']:
    movies[col] = movies[col].apply(collapse)

movies['overview'] = movies['overview'].apply(lambda x: x.split())

movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

hollywood_df = movies[['movie_id','title','tags']]
hollywood_df['tags'] = hollywood_df['tags'].apply(lambda x: " ".join(x))
hollywood_df['industry'] = "hollywood"


# BOLLYWOOD
bolly = pd.read_csv("BollywoodMovieDetail.csv")

if 'overview' in bolly.columns:
    bolly['tags'] = bolly['overview']
elif 'description' in bolly.columns:
    bolly['tags'] = bolly['description']
else:
    bolly['tags'] = bolly.iloc[:,1]

bolly = bolly[['title','tags']]
bolly.dropna(inplace=True)

bolly['tags'] = bolly['tags'].apply(lambda x: str(x))
bolly['movie_id'] = range(100000, 100000 + len(bolly))
bolly['industry'] = "bollywood"


# COMBINE
final_df = pd.concat([hollywood_df, bolly], ignore_index=True)
final_df['tags'] = final_df['tags'].apply(lambda x: x.lower())

# TF-IDF
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
vectors = tfidf.fit_transform(final_df['tags']).toarray()

similarity = cosine_similarity(vectors)

#SAVE
pickle.dump(final_df, open('movies.pkl','wb'))
pickle.dump(similarity, open('similarity.pkl','wb'))

print("DONE ✅")