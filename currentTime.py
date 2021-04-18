from datetime import datetime
from configFile import secrets


# Strftime codes cand be found way down at https://www.programiz.com/python-programming/datetime/strftime


class TodayStuff:
    def __init__(self):
        self.today = datetime.now()  # Takes new date and time reading each time class is used

    def givedate(self):
        #                       Wkday, Month, Day
        date = self.today.strftime('%A %B %d')  # Defines var as a fstring with the date put in
        return date  # Returns string to be spoken

    def givetime(self):
        # Defines var as a fstring with the time put in
        if secrets["Clock Format"] == "24hr":
            # 24 hour clock            Hour, Minute
            time = self.today.strftime('%H:%M')
        else:
            # 12 hour clock         Hour, Minute, AM/PM
            time = self.today.strftime('%I:%M %p')

        return time  # Returns string to be spoken
