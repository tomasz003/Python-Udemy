import requests, smtplib, time
from datetime import datetime

#my parameters
MY_LAT = 49.192199
MY_LONG = 20.503213
LOCAL_UTC_OFFSET = 2
MY_EMAIL="test00mail0000@gmail.com"
PASSWORD= "dlwy bvtk ocie ykwv"

def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour


def iss_is_close(lat, long):
    is_close=(abs(MY_LAT-lat)<=5)*(abs(MY_LONG-long)<=5)
    return is_close

def is_dark(cur_time):
    if cur_time>lt_sunset or cur_time<lt_sunrise:
        return True
    return False

#ISS tracking
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#daytime tracking
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
lt_sunrise = utc_to_local(sunrise)
lt_sunset = utc_to_local(sunset)

hour_now = datetime.now().hour

while True:
    time.sleep(60)
    if iss_is_close(MY_LAT, MY_LONG) and is_dark(hour_now):
        # sending letter
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:Look up!!!\n\nThe ISS is close!\nIts coordinates: {iss_latitude}, {iss_longitude}\nTry to find it!")




