def calc_area():
    print("Flächenrechner: ")
    try:
        breite = float(input("gib die Breite an: "))
        hoehe = float(input("gib die Länge an: "))
        flaeche = breite * hoehe
        print(f"Die Fläche des Rechtecks beträgt {flaeche} Quadratmeter")
    except ValueError:
        print("Bitte Zahlen eingeben mit denen ich arbeiten kann!")
    print("\n")


def miles_to_km():
    print("Meilen zu Kilometer: ")
    try:
        meilen = float(
            input("Gib die Meilen an, die du in KM umgerechnet haben willst: ")
        )
        km = meilen * 1.60934
        print(f"{meilen} Meilen sind {km:.2f} Kilometer.")
    except ValueError:
        print("Bitte Zahlen eingeben mit denen ich arbeiten kann!")
    print("\n")


def km_to_miles():
    print("Kilometer zu Meilen Rechner: ")
    try:
        km = float(
            input("Gib die Kilometer ein, die du in Meilen umgerechnet haben willst: ")
        )
        meilen = km * 0.621371
        print(f"{km} Kilometer sind {meilen:.2f} Meilen.")
    except ValueError:
        print("Bitte Zahlen eingeben mit denen ich arbeiten kann!")
    print("\n")


def celsius_to_fahrenheit():
    print("Celsius zu Fahrenheit Rechner: ")
    try:
        celsius = float(input("Gib die Temperatur in Celsius ein: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius}°C entsprechen {fahrenheit:.2f}°F.")
    except ValueError:
        print("Bitte Zahlen eingeben mit denen ich arbeiten kann!")
    print("\n")


def fahrenheit_to_celsius():
    print("Fahrenheit zu Celsius Rechner: ")
    try:
        fahrenheit = float(input("Gib die Temperatur in Fahrenheit ein: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit}°F entsprechen {celsius:.2f}°C.")
    except ValueError:
        print("Bitte Zahlen eingeben mit denen ich arbeiten kann!")
    print("\n")


def menue():
    while True:
        print("Willkommen zu den Rechnern!")
        print("1. Flächenrechner (Rechteck)")
        print("2. Meilen zu Kilometer")
        print("3. Kilometer zu Meilen")
        print("4. Celsius zu Fahrenheit")
        print("5. Fahrenheit zu Celsius")
        print("6. Beenden")

        auswahl = input("Wähle eine Option (1/2/3/4/5/6): ")

        if auswahl == "1":
            calc_area()
        elif auswahl == "2":
            miles_to_km()
        elif auswahl == "3":
            km_to_miles()
        elif auswahl == "4":
            celsius_to_fahrenheit()
        elif auswahl == "5":
            fahrenheit_to_celsius()
        elif auswahl == "6":
            print("Programm beendet.")
            break
        else:
            print("Bitte versuche es erneut.")


if __name__ == "__main__":
    menue()
