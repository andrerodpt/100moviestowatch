import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()
movies_html = response.text

soup = BeautifulSoup(movies_html, 'html.parser')

titles = soup.select(selector=".article-title-description .title")
titles_final_list = []
for title in titles:
    titles_final_list.insert(0, title.getText())

with open("movies.txt", "w", encoding="ISO-8859-1") as f:
    for title in titles_final_list:
        f.write(str(title) + "\n")