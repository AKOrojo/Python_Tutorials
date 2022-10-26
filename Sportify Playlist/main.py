import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(response.text, 'html.parser')

test = []
song_list = []

songs = soup.find_all("h3", class_="a-no-trucate")

for tag in songs:
    test.append(tag.getText())

for song in test:
    song_list.append(song.replace("\n", ""))

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id="SECERT",
        client_secret="ID",
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
print(result)

try:
    uri = result["tracks"]["items"][0]["uri"]
    song_uris.append(uri)
except IndexError:
    print(f"{song} doesn't exist in Spotify. Skipped.")
