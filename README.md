# 🎬 TMDb Movie Scraper & Data Analysis

An automated Python pipeline designed to extract, clean, and analyze global movie metadata using the TMDb API.

## 📌 Project Overview
This project demonstrates a full data analytics lifecycle. It programmatically fetches 1,500+ records, stores them in a structured CSV, and utilizes **Pandas** for data processing.

## 🛠️ Tech Stack
- **Languages:** Python 3.13
- **APIs:** The Movie Database (TMDb)
- **Libraries:** Pandas, Requests, Python-Dotenv

## 📂 Project Structure
- `scripts/`: Python automation for API data extraction.
- `data/`: Local CSV storage for extracted metadata.
- `notebooks/`: Jupyter Notebooks for Exploratory Data Analysis (EDA).

## 🚀 Setup & Usage
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory.
4. Add your API key: `TMDB_API_KEY=your_key_here`.
5. Run the scraper: `python scripts/imdb_scraper.py`.