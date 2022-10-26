from bs4 import BeautifulSoup
import requests

movies_list = []

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

movies_names = soup.find_all(name="h3", class_="title")

for movie in movies_names:
    movies_list.append(movie.getText())

movies_list.reverse()

with open('Web Scraper/movies_list.txt', 'w', encoding="utf-8") as fp:
    fp.write('\n'.join(movies_list))
