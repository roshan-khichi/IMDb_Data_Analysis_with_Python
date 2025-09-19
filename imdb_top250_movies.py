import gettext
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd
import random

# base url
url = "https://www.imdb.com/chart/top/"

# Launch Chrome
proxies = [
"222.252.194.29:8080",
"35.193.78.97:8080",
"200.174.198.158:8888",
"57.129.81.201:999",
"5.78.130.46:12016"
]

# Randomly select a proxy
proxy = random.choice(proxies)
chrome_options = Options()

chrome_options.add_argument(f'--proxy-server={proxy}')

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)
# wait for page to load (important for dynamic sites)
time.sleep(3)

# Get full page source
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Example: extract movie titles
movies = soup.select("div.ipc-metadata-list-summary-item__c")  # CSS selector for movie headings

movie_list=[]
for movie in movies:  
    movie_title = movie.h3.getText().split(". ",1)[1];
    ratings= movie.select_one("span.ipc-rating-star--rating").getText();
    ratings_count = movie.select_one("span.ipc-rating-star--voteCount").getText().split("(")[1].split(")")[0];
    year = movie.select("span.cli-title-metadata-item");
    data = {
            # "place": place,
            "movie_title": movie_title,
            "rating": ratings,
            "rating count": ratings_count,
            "year": year[0].getText(),
            "time": year[1].getText()
            }
    movie_list.append(data)

df = pd.DataFrame(movie_list)
df.to_csv('imdb_top_250_movies.csv',index=False)

print("IMDb page saved.")

driver.quit()
