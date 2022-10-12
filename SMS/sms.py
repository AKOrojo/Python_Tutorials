import requests

APIKEY = "1f111ca20b1044a3f1adc918589efe9a"
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 57,
    "lon": -2.15,
    "appid": APIKEY
}

response = requests.get(
    url=OWN_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

id = weather_data["list"][:6]

for hour_d in id:
    x = hour_d["weather"][0]["id"]
if x < 700:
    print("UMBRELLA")
