from pyowm.owm import OWM

cityName = "City"  # The name of your city/town
countryCode = "CC"  # The code of your country in all caps, if you live in the US its your state's abbreviation
apiKey = "API Key"  # The API key you generated from OpenWeatherMap

# Set up lines
owm = OWM(apiKey)
reg = owm.city_id_registry()

# Getting the cities IDs meeting the given criteria
cityIDs = reg.ids_for(cityName, country=countryCode)
print(f"{cityIDs}\n")

# Getting the city locations meeting the given criteria
cityLocations = reg.locations_for(cityName, country=countryCode)
for i in cityLocations:
    print(f"ID= {i.id}, Latitude= {i.lat}, Longitude= {i.lon}")
