# imports
import requests
import datetime as df

# Constants
GENDER = "male"
WEIGHT_KG = 82
HEIGHT_CM = 175.5
AGE = 23

# Variables
today = df.datetime.now()

# nutritionix api
APP_ID = "1f226b0b"
API_KEY = "f3f765a476eaae689c543e6d7ec99dbf"
Exercise_Endpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

nutritionix_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

nutritionix_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nutritionix_response = requests.post(
    url=Exercise_Endpoints, json=nutritionix_params, headers=nutritionix_header)
result = nutritionix_response.json()

# sheety
sheety_endpoint = "https://api.sheety.co/ead6afd6ebc02a3b7a6d36f580a85dde/myWorkouts/workouts"
headers = {"Authorization": "Bearer MYREALLYLONGTOKENIGOT"}

excercise_array = result["exercises"]
for exercises in excercise_array:
    Exercise = exercises["name"]
    Duration = exercises["duration_min"]
    Calories = exercises["nf_calories"]

    shetty_params = {
        "workout": {
            "date": today.strftime("%Y/%m/%d"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": Exercise.title(),
            "duration": Duration,
            "calories": Calories
        }
    }

    sheety_response = requests.post(
        url=sheety_endpoint, json=shetty_params, headers=headers)
    sheety_response.raise_for_status()
