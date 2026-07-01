import requests
import os
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path

load_dotenv()
token = os.getenv("TMDB_BEARER_TOKEN")

output_dir = Path("../bronze")

url = "https://api.themoviedb.org/3/genre/movie/list"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers, timeout=(5, 30))
print(response.status_code)

df = pd.DataFrame(response.json())
print(len(df))

df.to_csv(output_dir/"movies_genres.csv")