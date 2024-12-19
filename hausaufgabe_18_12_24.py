# 1. Aktuelles Datum und Uhrzeit ausgeben:
# Importiere das datetime-Modul.
# ○Erstelle eine Funktion aktuelles_datum_und_uhrzeit(), die das
# aktuelle Datum und die aktuelle Uhrzeit im Format TT.MM.JJJJ HH:MM:SS
# ausgibt

import datetime
import calendar

# import locale

# def current_date_time():
#     # das aktuelle Datum und Uhrzeit
#     jetzt = datetime.datetime.now()
#     # Formatieren in TT.MM.JJJJ HH:MM:SS
#     # strftime wandelt Datum & Uhrzeit in string um und strptime von string zu Datum & Uhrzeit
#     jetzt.strftime("%d.%m.%Y %H:%M:%S")
#     return jetzt


# # Aufruf der Funktion
# print(current_date_time())

# 2. Differenz bis zum Jahresende berechnen:
# Schreibe eine Funktion tage_bis_jahresende(), die die Anzahl der Tage
# vom aktuellen Datum bis zum 31. Dezember des aktuellen Jahres berechnet.
# Hinweis: Verwende datetime.date oder datetime.datetime zur
# Berechnung.


# def tage_bis_jahresende():
#     heute = datetime.date.today()
#     jahresende = datetime.date(2024, 12, 31)
#     result = (jahresende - heute).days
#     return print(f"Noch {result} bis zum Jahresende!")


# tage_bis_jahresende()

# 3. Benutzerdefiniertes Datum:
# Implementiere eine Funktion tage_bis_datum(), die ein vom Benutzer
# eingegebenes Datum im Format TT.MM.JJJJ einliest und die Anzahl der
# Tage vom aktuellen Datum bis zu diesem Datum berechnet.
# Tipp: Verwende input() für die Benutzereingabe und prüfe, ob das
# eingegebene Datum gültig ist. Falls nicht, soll der Benutzer eine neue Eingabe
# machen.


# def tage_bis_datum():
#     try:
#         # Benutzer nach Eingabe des Datums fragen
#         dein_datum = input("Bitte gib ein Datum im Format TT.MM.JJJJ ein: ")
#         # Eingabe in ein Datum umwandeln
#         ich_strp_dein_datum = datetime.datetime.strptime(dein_datum, "%d.%m.%Y")
#         # Heutiges Datum abrufen
#         heute = datetime.datetime.today()
#         # Differenz in Tagen berechnen
#         ergebnis = abs(heute - ich_strp_dein_datum).days
#         return print(f" Es sind noch {ergebnis} Tage bis zu deinem angegebenen Datum")
#     except ValueError:
#         # Fehlerbehandlung bei ungültiger Eingabe
#         print("Fehler! Bitte gib ein Datum im richtigen Format TT.MM.JJJJ ein.")


# tage_bis_datum()

# 4. Wochentag berechnen:
# Erstelle eine Funktion wochentag_berechnen(), die den Wochentag für ein
# beliebiges eingegebenes Datum berechnet und ausgibt (z. B. Montag,w
# Dienstag usw.).

# Frage an Tom, wieso gibt er mir falsche Werte für die Zukunft aus?


# def wochentag_berechnen():
#     wochentag = input("Bitte nenne ein Datum ")
#     day = datetime.datetime.strptime(wochentag, "%d.%m.%Y").date()
#     print(f"Der {wochentag} ist ein {calendar.day_name[day.weekday()]}\n")


# wochentag_berechnen()

# 5. Zeitverschiebung berechnen:
# Implementiere eine Funktion zeit_in_zukunft(), die eine Eingabe von
# Minuten, Stunden oder Tagen vom Benutzer entgegennimmt und das Datum
# und die Uhrzeit berechnet, die nach dieser Zeitspanne liegt.
# Beispiel: Wenn der Benutzer 2 Stunden eingibt und die aktuelle Zeit 14:00
# ist, sollte das Programm 16:00 ausgeben.

from datetime import datetime, timedelta


def zeit_in_zukunft():
    print("Gib die Zeitspanne ein, die du hinzufügen möchtest:")
    print("1: Minuten")
    print("2: Stunden")
    print("3: Tage")

    try:
        # Benutzer wählen lassen, welche Einheit er hinzufügen möchte
        wahl = int(input("Wähle die Einheit (1, 2 oder 3): "))

        # Benutzer nach der Anzahl der Einheiten fragen
        anzahl = int(input("Wie viele Einheiten möchtest du hinzufügen? "))

        # Aktuelles Datum und Uhrzeit abrufen
        jetzt = datetime.now()

        # Zeitspanne berechnen basierend auf der Auswahl
        if wahl == 1:  # Minuten
            zukunft = jetzt + timedelta(minutes=anzahl)
        elif wahl == 2:  # Stunden
            zukunft = jetzt + timedelta(hours=anzahl)
        elif wahl == 3:  # Tage
            zukunft = jetzt + timedelta(days=anzahl)
        else:
            print("Ungültige Wahl. Bitte wähle 1, 2 oder 3.")
            return

        # Ergebnis ausgeben
        print(f"Aktuelle Zeit: {jetzt.strftime('%d.%m.%Y %H:%M:%S')}")
        print(f"Zeit in der Zukunft: {zukunft.strftime('%d.%m.%Y %H:%M:%S')}")

    except ValueError:
        print("Fehler: Bitte gib eine gültige Zahl ein.")


# Funktion aufrufen
zeit_in_zukunft()
