import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv

# 1. Initialize environment variables
# This looks for the .env file in the root directory
load_dotenv()

# 2. Securely retrieve the API key
# The key is no longer written here; it is pulled from your .env file
API_KEY = os.getenv("TMDB_API_KEY")

# Safety Check: If the key is missing, stop the script immediately
if not API_KEY:
    print("❌ ERROR: TMDB_API_KEY not found in .env file.")
    print("Please ensure your .env file exists and contains: TMDB_API_KEY=your_key_here")
    exit()

print("✅ API Key successfully loaded. Starting the data collection...")

# List to store all movie data
all_movies = []

# Loop through pages to get popular movies
# TMDb returns 20 movies per page. We loop 75 pages to get ~1500 movies
for page in range(1, 76):
    print(f"Fetching page {page} of 75...")
    list_url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&page={page}"
    
    try:
        response = requests.get(list_url)
        
        # Check if the request was successful
        if response.status_code != 200:
            print(f"⚠️ Warning: Could not fetch page {page}. Status Code: {response.status_code}")
            continue
            
        data = response.json()
        results = data.get("results", [])
        
        # Loop through each movie to get more detailed info
        for movie in results:
            movie_id = movie['id']
            
            # Detail API call for each movie (to get budget, revenue, and genres)
            detail_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
            detail_response = requests.get(detail_url)
            
            if detail_response.status_code == 200:
                d = detail_response.json()
                
                # Store cleaned movie info in the list
                all_movies.append({
                    'id': d.get('id'),
                    'title': d.get('title'),
                    'release_date': d.get('release_date'),
                    'status': d.get('status'),
                    'original_language': d.get('original_language'),
                    'vote_average': d.get('vote_average'),
                    'vote_count': d.get('vote_count'),
                    'popularity': d.get('popularity'),
                    'budget': d.get('budget', 0),
                    'revenue': d.get('revenue', 0),
                    'runtime': d.get('runtime', 0),
                    'genres': ", ".join([g['name'] for g in d.get('genres', [])])
                })
            
            # Short delay to respect TMDb rate limits
            time.sleep(0.05)
            
    except Exception as e:
        print(f"❌ Error on page {page}: {e}")

# 3. Save all collected data into a CSV file
# We use os.path to ensure it works across different operating systems
df = pd.DataFrame(all_movies)

# Define the output path
output_file = os.path.join(os.path.dirname(__file__), "../data/tmdb_1500_movies_all_languages.csv")

# Save the CSV
df.to_csv(output_file, index=False)

print("-" * 30)
print(f"🚀 Success! {len(df)} movies saved to: {output_file}")