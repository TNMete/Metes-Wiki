# Aktuelles Datum und Uhrzeit ausgeben:
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

# Differenz bis zum Jahresende berechnen:
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

# Benutzerdefiniertes Datum:
# Implementiere eine Funktion tage_bis_datum(), die ein vom Benutzer
# eingegebenes Datum im Format TT.MM.JJJJ einliest und die Anzahl der
# Tage vom aktuellen Datum bis zu diesem Datum berechnet.
# Tipp: Verwende input() für die Benutzereingabe und prüfe, ob das
# eingegebene Datum gültig ist. Falls nicht, soll der Benutzer eine neue Eingabe
# machen.


# def tage_bis_datum():
#     dein_datum = input("gib Datum!")
#     ich_strp_dein_datum = datetime.datetime.strptime(dein_datum, "%d.%m.%Y")
#     heute = datetime.datetime.today()
#     ergebnis = abs(heute - ich_strp_dein_datum).days
#     return print(f" Es sind noch {ergebnis} bis zu deinem angegebenen Datum")


# tage_bis_datum()

# Wochentag berechnen:
# Erstelle eine Funktion wochentag_berechnen(), die den Wochentag für ein
# beliebiges eingegebenes Datum berechnet und ausgibt (z. B. Montag,
# Dienstag usw.).

# Frage an Tom, wieso gibt er mir falsche Werte für die Zukunft aus?

# print("Bitte nenne mir ein Datum (TT.MM.JJJJ): ")
# datum = input()
# # in Datumformat konvertieren
# datum = datetime.datetime.strptime(datum, "%d.%m.%Y").date()
# print("Dein gewähltes Datum ist ein " + calendar.day_name[datum.weekday()])

# Zeitverschiebung berechnen:
# Implementiere eine Funktion zeit_in_zukunft(), die eine Eingabe von
# Minuten, Stunden oder Tagen vom Benutzer entgegennimmt und das Datum
# und die Uhrzeit berechnet, die nach dieser Zeitspanne liegt.
# Beispiel: Wenn der Benutzer 2 Stunden eingibt und die aktuelle Zeit 14:00
# ist, sollte das Programm 16:00 ausgeben.
