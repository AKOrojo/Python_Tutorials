from unittest import result
import requests

# CONSTANTS
SHEETY_ENDPOINT_GET = "https://api.sheety.co/ead6afd6ebc02a3b7a6d36f580a85dde/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.headers = {"Authorization": "Bearer MYREALLYLONGTOKENIGOT"}
        self.url_endpoint_get = SHEETY_ENDPOINT_GET
        self.result_data = []

    def request(self):
        sheety_response = requests.get(
            url=self.url_endpoint_get, headers=self.headers)
        sheety_response.raise_for_status()
        self.result_data = sheety_response.json()["prices"]
        return self.result_data

    def update(self, update_info, country):
        for sub in self.result_data:
            if sub['city'] == country.title():
                id = sub["id"]
        data = {
            "price": {
                "iataCode": update_info
            }
        }

        endpoint = f"{SHEETY_ENDPOINT_GET}/{id}"
        response = requests.put(url=endpoint, json=data, headers=self.headers)
        response.raise_for_status()
