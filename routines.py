from currentTime import TodayStuff
from generateSpeech import syn_speech
from weather import WeatherData


# This program just simplifies my voice commands options


class Routines:
    def __init__(self):
        self.today_class = TodayStuff()
        self.weather_class = WeatherData()

    def get_datetime(self):
        # Necessary to call this each time to get information
        # Call and then put [0] for date or [1] for time directly after it
        date = self.today_class.givedate()
        time = self.today_class.givetime()

        date_time_list = [date, time]  # Puts values in list so I can return both
        return date_time_list

    def get_weather(self):
        # Necessary to call this each time to get information
        # Call and then put [0] for temp and [1] for status
        status = self.weather_class.weather_status()
        temp = self.weather_class.feels_like()

        weather_list = [temp, status]  # Puts values in list so I can return all of them
        return weather_list

    def get_bread(self):
        # Morning routine, will be activated by saying Jarvis
        print("Good morning Jorden, beautiful day isn't it?")
        syn_speech("Good morning Jorden, beautiful day isn't it?")

        print(f"Today is {self.get_datetime()[0]}, and it is currently {self.get_datetime()[1]}.")
        syn_speech(f"Today is {self.get_datetime()[0]}, and it is currently {self.get_datetime()[1]}.")

        print(f"Outside, it feels like {self.get_weather()[0]} with {self.get_weather()[1]}.")
        syn_speech(f"Outside, it feels like {self.get_weather()[0]} with {self.get_weather()[1]}.")

        print("It's time to wake up and work hard . . . . . . Lets get this bread!")
        syn_speech("It's time to wake up and work hard . . . . . . Lets get this bread!")
