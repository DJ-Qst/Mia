from routines import Routines
from generateSpeech import syn_speech
from configFile import secrets

# Date/Time: get_datetime() and [0]=date or [1]=time
# Weather: get_weather() and [0]=temp or [1]=status


# Where the actual programming goes
if __name__ == '__main__':
    # IMPORTANT: There are no prebuilt messages so things like get_weather()[0] have no extra words, its only values
    # You have to construct messages with f strings
    while True:
        action = str.lower(input(f"{secrets['Name']}: "))
        if "get" and "bread" in action:
            # Creates a routines instance and runs the Lets Get This Bread routine
            routines = Routines()
            routines.get_bread()

        elif "date" or "time" or "temperature" or "status" in action:
            # Creates a routines instance and decides on what to say
            routines = Routines()
            speechList = []  # List to store messages

            # Cycling through each keyword to find matches and then appending them to the list
            if "date" in action:
                speechList.append(f"Today is {routines.get_datetime()[0]}")
            if "time" in action:
                speechList.append(f"The current time is {routines.get_datetime()[1]}")
            if "temperature" in action:
                speechList.append(f"It feels like {routines.get_weather()[0]}")
            if "status" in action:
                speechList.append(f"It is a beautiful day outside with {routines.get_weather()[1]}")

            # Joining all of the messages with blank space and then speaking them
            message = " ".join(speechList)
            syn_speech(message)

        elif action == "exit":
            break
