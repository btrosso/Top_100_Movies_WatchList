import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_webpage = response.text
soup = BeautifulSoup(movies_webpage, "html.parser")

titles = soup.find_all(name="h3", class_="title")
titles_text = [title.getText() for title in titles]

with open("movies.txt", mode="w", encoding="utf-8") as movie_file:
    for title in reversed(titles_text):
        movie_file.write(f"{title}\n")
