import requests
import os
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path

load_dotenv()
token = os.getenv("TMDB_BEARER_TOKEN")

input_dir = Path("../bronze")/"movies.csv"
output_dir = Path("../bronze")

url = "https://api.themoviedb.org/3/movie/"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json"
}

movies_csv = pd.read_csv(input_dir)
movies_details = []

for id in movies_csv["id"]:
    try:
        response = requests.get(url + str(id), headers=headers, timeout=(5, 30))
        print(response.status_code)
        for movie_details in response.json().get("results", []):
            movies_details.append(movie_details)

    except Exception as e:
        print(f"Erro ao coletar filmes: {e}")
        break

df = pd.DataFrame(movies_details)
print(len(movies_details))

df.to_csv(output_dir/"movies_details.csv")
