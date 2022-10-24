# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch


ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
flight_location = data_manager.request()


for cities in flight_location:
    if cities["iataCode"] == "":
        term = cities["city"]
        code = flight_search.get_loc(city_name=term)

        data_manager.update(update_info=code, country=term)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in flight_location:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
