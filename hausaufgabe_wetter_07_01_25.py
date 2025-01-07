import requests

response = requests.get("https://wttr.in/Koeln?format=j1")
daten = response.json()

print(daten["current_condition"])

temp = daten["current_condition"][0]["temp_C"]
felt_temp = daten["current_condition"][0]["FeelsLikeC"]
location = daten["nearest_area"][0]["areaName"][0]["value"]

print(
    f"Die aktuelle Temperatur in {location} beträgt {temp}°C und die gefühlte Temperatur beträgt {felt_temp}°C"
)
