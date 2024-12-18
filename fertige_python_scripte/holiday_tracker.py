# folgender Befehl checkt ob du heute "Urlaub" hast
# from datetime import datetime

# date = datetime(2024, 12, 24)
# print(date)

date = input("enter the date you want to check e.g. 2024.12.13: ")

its_winter_holidays = date >= datetime(2024, 12, 24) and date <= datetime(2025, 1, 2)
its_easter_holidays = date >= datetime(2025, 4, 18) and date <= datetime(2025, 4, 21)
its_summer_holidays = date >= datetime(2025, 8, 11) and date <= datetime(2025, 8, 19)
its_winter2_holidays = date >= datetime(2025, 12, 24) and date <= datetime(2026, 1, 1)
# mein Urlaub
its_japan_holidays = date >= datetime(2025, 2, 25) and date <= datetime(2025, 2, 29)

feiertage = datetime[
    "2024.10.03",
    "2024.10.31",
    "2024.12.25",
    "2024.12.26",
    "2025.01.01",
    "2025.04.18",
    "2025.04.21",
    "2025.05.01",
    "2025.05.29",
    "2025.06.09",
    "2025.10.03",
    "2025.10.31",
    "2025.12.25",
    "2025.12.26",
    "2026.01.01",
]

if its_winter_holidays:
    print("you have winter holidays!")
elif its_easter_holidays:
    print("you have easter holidays!")
elif its_summer_holidays:
    print("you have summer holidays!")
elif its_winter2_holidays:
    print("you have winter holidays!")
elif its_japan_holidays:
    print("you'll be in Japan during that time!")
elif date in feiertage:
    print("Dieses Datum ist ein Feiertag!")
else:
    print("An diesem Tag hast du leider keinen Urlaub oder Feiertag :(")
