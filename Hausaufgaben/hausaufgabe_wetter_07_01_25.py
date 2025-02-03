import requests

ort = input("Welche Stadt möchtest du abfragen?: ")
response = requests.get(f"https://wttr.in/{ort}?format=j1")
daten = response.json()

print(daten["current_condition"])

temp = daten["current_condition"][0]["temp_C"]
felt_temp = daten["current_condition"][0]["FeelsLikeC"]
location = daten["nearest_area"][0]["areaName"][0]["value"]

print(
    f"Die aktuelle Temperatur in {location} beträgt {temp}°C und die gefühlte Temperatur beträgt {felt_temp}°C"
)
