import requests
import os
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path

load_dotenv()
token = os.getenv("TMDB_BEARER_TOKEN")

output_dir = Path("../bronze")

url = "https://api.themoviedb.org/3/discover/movie"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json"
}

params = {
    "primary_release_date.gte": "2020-01-01",
    "vote_count.gte": 100,
    "include_adult": False,
    "include_video": False,
    "sort_by": "popularity.desc",
    "page": 1
}

movies = []
movie_titles = set()

while len(movies) < 1000:
    try:
        response = requests.get(url, headers=headers, params=params, timeout=(5, 30))
        print(response.status_code)

    except Exception as e:
        print(f"Erro ao coletar filmes: {e}")
        break

    for movie in response.json().get("results", []):
        if len(movies) < 1000: 
            if movie["title"] not in movie_titles:
                movies.append(movie)
                movie_titles.add(movie["title"])
    
    params["page"] += 1

df = pd.DataFrame(movies)
print(len(movies))

df.to_csv(output_dir/"movies.csv")