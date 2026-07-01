import requests
import os
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path
import concurrent.futures

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

def load_url(url, headers, timeout):
    response = requests.get(url, headers=headers, timeout=timeout)
    print(response.status_code)
    return response.json()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    future_to_url = {}

    for movie_id in movies_csv["id"]:
        movie_url = url + str(movie_id)
        future = executor.submit(load_url, movie_url, headers, (5, 30))
        future_to_url[future] = movie_url
    
    for future in concurrent.futures.as_completed(future_to_url):
        try: 
            movie_url = future_to_url[future]
            data = future.result()
            movies_details.append(data)
        except Exception as e:
            print(e)

df = pd.DataFrame(movies_details)
print(len(movies_details))

df.to_csv(output_dir/"movies_details.csv")
