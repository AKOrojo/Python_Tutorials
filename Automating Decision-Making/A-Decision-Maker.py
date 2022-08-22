import requests
import random
import pandas

response = requests.get("http://discord.jikan.moe")

choice = (random.randint(0, 1000))
anime = requests.get(f"https://api.jikan.moe/v4/anime/{choice}/full")
print(anime.json)
