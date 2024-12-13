date = input("enter the date you want to check e.g. 2024.12.13: ")

its_winter_holidays = date >= "2024.12.24" and date <= "2025.01.02"
its_easter_holidays = date >= "2025.04.18" and date <= "2025.04.21"
its_summer_holidays = date >= "2025.08.11" and date <= "2025.08.19"
its_winter2_holidays = date >= "2025.12.24" and date <= "2026.01.01"

feiertage = [
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
elif date in feiertage:
    print("Dieses Datum ist ein Feiertag!")
else:
    print("An diesem Tag hast du leider keinen Urlaub oder Feiertag :(")
