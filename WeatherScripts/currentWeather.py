from pyowm.owm import OWM
from configFile import secrets


# This program talks to Open Weather Map (OWM) weather manager to get current weather data and return it
# Usage Documentation can be found at https://pyowm.readthedocs.io/en/latest/v3/code-recipes.html#weather_data
# This is an example of what PyOWM is accessing: https://openweathermap.org/current#current_JSON

class CurrentWeatherData:
    def __init__(self):
        # Meta stuff to use
        self.owm = OWM(secrets["API Key"])  # This is your API key for OWM
        self.cityID = secrets["City ID"]  # This is your town's city ID
        self.mgr = self.owm.weather_manager()  # This is the manager of the weather information frm OWM
        self.weather = self.mgr.weather_at_id(self.cityID).weather  # This is the current weather of Ganado
        self.temp_list = self.weather.temperature(secrets["Temp System"])  # All temps including current and feels like

    def weather_status(self):
        status = self.weather.status  # Generic, non-detailed status, more of a category than anything

        # Adding an "a" before all status' except for clouds, best grammar I could make
        if status.lower() == "clouds":
            status = self.weather.detailed_status
        else:
            status = f"a {self.weather.detailed_status}"

        return status

    def feels_like(self):
        temp = str(round(int(self.temp_list["feels_like"])))  # Converts feel for rounding and then makes it a str again
        return temp
