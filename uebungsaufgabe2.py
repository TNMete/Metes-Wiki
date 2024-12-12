#1. Namensabfrage mit Input

firstname = input("Gib deinen Vornamen ein: ")
lastname = input("Gib deinen Nachnamen ein: ")

name_full = firstname +" "+ lastname

print(f"Der vollständige Name lautet: {name_full}" )

#2. Addition von Zahlen
a = float(input("Zahl 1: "))
b= float(input("Zahl 2: "))

c = (a + b)

print(f"Ergebnis: {c}")

#3. Zusatzaufgabe - Einfache If-Bedingung

zahl = float(input("Gib eine Zahl zum prüfen an:" ))

if zahl > 0:
    print("Die Zahl ist positiv.")
elif zahl == 0:
    print("Die Zahl ist null.")
else :
    print("Die Zahl ist negativ.")

istgerade = (zahl == 2 and zahl != -1) or (zahl % 2 == 0)

if istgerade:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")