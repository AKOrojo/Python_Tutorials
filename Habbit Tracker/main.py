from ctypes.wintypes import HENHMETAFILE
from tokenize import Token
from urllib import response
import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "banny"
TOKEN = "atbdyjdkknjndjs"
ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "cycling",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

header = {
    "X-USER-TOKEN": TOKEN
}
#responses = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(responses)

today = datetime.datetime.now()
x = today.strftime("%Y%m%d")

pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.68"
}

#responses1 = requests.post(url=pixel_post_endpoint,json=post_config, headers=header)
# print(responses1.text)

put_config = {
    "quantity": "17.68"
}

pixel_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{x}"

responses2 = requests.put(url=pixel_put_endpoint,
                          json=put_config, headers=header)
print(responses2.text)
