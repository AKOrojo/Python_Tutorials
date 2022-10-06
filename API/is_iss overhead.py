from pickle import TRUE
import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position


def iss_porsition():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False

# and it is currently dark


def is_night():
    if sunset <= time_now.hour or sunrise >= time_now.hour:
        return True
    else:
        return False


# Then send me an email to tell me to look up.
if iss_porsition() and is_night():
    my_emails = "b.korojo@gmail.com"
    my_passwords = "abcd1234()"

    with smtplib.SMTP("smtp.gmail.com") as connections:
        connections.starttls()
        connections.login(user=my_emails, password=my_passwords)
        connections.sendmail(from_addr=my_emails, to_addr="123@gmail.com",
                             msg="Subject:Hello\n\n This is the email body")


# BONUS: run the code every 60 seconds.
time.sleep(60000)
