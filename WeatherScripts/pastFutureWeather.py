import requests
from configFile import secrets
from datetime import datetime


# This program talks to Open Weather Map (OWM) OneCall API to get the past and future weather data and return it
# I use requests here because the PyOWM OneCall library documentation isn't great, and I couldn't figure it out.
# Usage documentation can be found at: https://openweathermap.org/api/one-call-api

def make_current_request(key, lat, lon, system):
    if str.lower(system) == "fahrenheit":
        system = "imperial"
    elif str.lower(system) == "celsius":
        system = "metric"
    r = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?"
                     f"lat={lat}&lon={lon}&exclude=current,minutely&appid={key}&units={system}")
    r = r.json()
    today = r["daily"][0]
    sunrise = datetime.utcfromtimestamp(today["sunset"]).strftime("%m-%d-%Y  %H:%M")
    print(sunrise)


make_current_request(secrets["API Key"], secrets["City LatLon"][0], secrets["City LatLon"][0], secrets["Temp System"])
