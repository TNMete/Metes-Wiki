# User, wählt 1-3 (schere, stein, papier)

# wir öffnen funktion:
# nimm user input
# lasse random.choice() wahl treffen
# vergleiche user wahl mit random wert (schere>papier, stein>schere, papier>stein)
# return: zeige ergebnis

import random


def spiel(spielereingabge):

    gewonnen = False
    verloren = False

    # coinflip = random.choice([“Schere”, “Stein”, “Papier”])
    eins_davon = ["Schere", "Stein", "Papier"]
    coinflip = random.choice(eins_davon)

    print(f"Dein Gegner hat {coinflip} gewählt!")
    print(f"Du hast {spielereingabge} gewählt!")

    if spielereingabge == coinflip:
        print("Unentschieden!")
    elif spielereingabge == "Schere" and coinflip == "Papier":
        print("Gewonnen!")
        gewonnen = True
    elif spielereingabge == "Stein" and coinflip == "Schere":
        print("Gewonnen!")
        gewonnen = True
    elif spielereingabge == "Papier" and coinflip == "Stein":
        print("Gewonnen!")
        gewonnen = True
    else:
        print("Verloren :(")
        verloren = True
    return [gewonnen, verloren]


def menue():
    punktestand_spieler = 0
    punktestand_gegner = 0

    while True:
        ergebnis = []
        print("Wähle Schere, Stein oder Papier!\n")
        print("1. Schere")
        print("2. Stein")
        print("3. Papier")
        print("4. Beenden\n")

        auswahl = input("Wähle eine Option (1/2/3/4): ")
        print("\n")
        if auswahl == "1":
            ergebnis = spiel("Schere")
        elif auswahl == "2":
            ergebnis = spiel("Stein")
        elif auswahl == "3":
            ergebnis = spiel("Papier")
        elif auswahl == "4":
            print("Programm beendet.")
            # beendet Programm/script
            break
        else:
            print("Bitte versuche es erneut.")
            # continue = überspringt/beendet aktuelle Schleife
            continue
        if ergebnis[0]:
            punktestand_spieler += 1
        elif ergebnis[1]:
            punktestand_gegner += 1
        print("Der aktuelle Spielstand: ")
        print(f"Du {punktestand_spieler} - Gegner {punktestand_gegner}\n")


menue()
