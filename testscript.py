# rezepte = {
#     "Spiegelei": "Zutaten: Ei, Salz, Paprika & Pfeffer.",
#     "Salat": "Zutaten: Blattsalat, Tomaten, Gurken, Dressing.",
# }


# def zeige_rezepte():
#     print("Verfügbare Rezepte:")
#     rezept_liste = list(rezepte.keys())

#     for i, rezept in enumerate(rezept_liste, start=1):
#         print(f"{i}. {rezept}")

#     # Auswahl
#     try:
#         auswahl = int(input("Bitte die Nummer des Rezepts eingeben: ")) - 1
#         if 0 <= auswahl < len(rezept_liste):
#             rezept_name = rezept_liste[auswahl]
#             print(f"\nRezept für {rezept_name}:")
#             print(rezepte[rezept_name])
#         else:
#             print("Ungültige Auswahl. Bitte eine Nummer aus der Liste wählen.")
#     except ValueError:
#         print("Bitte eine gültige Zahl eingeben.")


# zeige_rezepte()


# NEUER TEST:

# zahlen = [45, 23, 666, 124551, 5, 6, 7, 8, 9]


# def verarbeite_liste(zahlen):
#     summe = sum(zahlen)

#     ungerade_zahlen = [zahl for zahl in zahlen if zahl % 2 != 0]

#     groesste_zahl = max(zahlen)

#     print("Summe der Zahlen:", summe)
#     print("Ungerade Zahlen:", ungerade_zahlen)
#     print("Größte Zahl in der Liste:", groesste_zahl)


# verarbeite_liste(zahlen)
