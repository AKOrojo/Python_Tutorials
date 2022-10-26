from importlib.resources import contents
from bs4 import BeautifulSoup

with open("Web Scraper/website.html", encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
print(soup.title.string)
print(soup.prettify())
anchor_tag = soup.find_all(name="a")
print(anchor_tag)

for tag in anchor_tag:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="id")

heading = soup.find(name="h1", class_="heading")

company_url = soup.select_one(selector="p a")
