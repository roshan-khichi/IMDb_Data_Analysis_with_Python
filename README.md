# 🎬 Movie & TV Show Data Analysis with Python
## 📌 Overview

This project demonstrates web scraping + data analysis + visualization using Python.
I scraped IMDb Movie/TV Show data (titles, ratings, genres, actors, runtime, etc.), cleaned it with Pandas, and explored interesting insights such as:

- 📊 Top-rated movies by genre  
- 👨‍🎤 Most successful actors and directors  
- 📅 Movie release trends over the years  
- 🎞️ Runtime and rating correlations  

The project also includes interactive visualizations and can be extended into a Movie Recommendation System or Review Sentiment Analyzer.

## 🚀 Features

✅ Web scraping of IMDb movie/TV show data using BeautifulSoup / Requests
✅ Data cleaning and preprocessing with Pandas
✅ Exploratory Data Analysis (EDA)
✅ Visualizations with Matplotlib & Seaborn
✅ Insights like:
  - Top 10 movies per genre
  - Highest-rated actors/directors
  - Trends in movie releases

---

## 🛠️ Tech Stack
Python 3

### Libraries:
- `pandas` → Data analysis  
- `requests` / `BeautifulSoup` → Web scraping (static pages)  
- `selenium` → Web scraping (JavaScript-rendered pages, auto browser handling)  
- `matplotlib` / `seaborn` → Visualization

## 📊 Example Visualizations

<img width="600" height="400" alt="Figure_1" src="https://github.com/user-attachments/assets/7b691fae-bd67-4117-bbc0-3a214b011a4a" />

<img width="600" height="400" alt="Figure_2" src="https://github.com/user-attachments/assets/afe8c236-ec3e-4936-b816-9f164498baf4" />

<img width="600" height="400" alt="Figure_3" src="https://github.com/user-attachments/assets/f5ec6793-091c-4bf2-8950-cc140c3bab2c" />


```bash

📂 Project Structure
📁 movie-data-analysis
│── 📄 README.md
│── 📄 requirements.txt
│── 📄 movie_data_analysis.ipynb   # Jupyter Notebook with code
│── 📄 scraper.py                  # (Optional) Script for scraping
│── 📂 data/                       # Raw & cleaned datasets
│── 📂 visuals/                    # Exported graphs & plots
```

## ⚡ Getting Started
### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/movie-data-analysis.git
cd movie-data-analysis
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the notebook
Open **movie_data_analysis.ipynb** in Jupyter Notebook / VSCode / Colab and run all cells.

4️⃣ For Selenium scraping
  Download [ChromeDriver]('https://chromedriver.chromium.org/downloads') matching your Chrome version, and update the path in **selenium_scraper.py**

## 🎯 Future Improvements

- Build a Streamlit Dashboard for interactive exploration
- Perform Sentiment Analysis on IMDb reviews
- Add a Recommendation System based on genres & actors

## 📝 License

This project is open-source and available under the MIT License
.

### ⚡ If you like this project, don’t forget to ⭐ the repo and share your feedback!
