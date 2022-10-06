import imp
import requests
import datetime

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
print(data['iss_position'])

parameters = {
    "lat": 51.587351,
    "lng": -0.127758,
    "formatted": 0}

response = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

time_now = datetime.datetime.now()
sunrise = data["results"]["sunrise"]
hours = sunrise.split("T")[1].split(":")[0]
print(hours, time_now.hour)
