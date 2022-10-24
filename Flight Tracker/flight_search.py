import requests
from flight_data import FlightData

LOCATION_QUERY_API = "zPMtWM0gdl3DlaLk_SSt1GAs8O4J7C-Y"
LOCATION_QUERY_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_loc(self, city_name):
        loc_headers = {
            "apikey": LOCATION_QUERY_API
        }

        location_params = {
            "term": city_name,
            "location_types": "city"
        }

        location = requests.get(
            url=LOCATION_QUERY_ENDPOINT, params=location_params, headers=loc_headers)
        code = location.json()["locations"][0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        loc_headers = {
            "apikey": LOCATION_QUERY_API
        }
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=loc_headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
