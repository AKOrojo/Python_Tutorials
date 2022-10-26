from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

a_tag = soup.find_all(name="span", class_="titleline")
utag = soup.find_all(name="span", class_="rank")

for tag in a_tag:
    a_tag_a = tag.find(name="a")
    print(a_tag_a.getText())
    print(a_tag_a.get("href"))
    print("\n\n")
