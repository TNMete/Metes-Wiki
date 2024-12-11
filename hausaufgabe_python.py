first_name = "Mete"
last_name = "Karaoglan"
age = "34"

zahl1 = 2
zahl2 = 10

print(first_name + " " + last_name + " " + age)

print("Zahl 1 + Zahl 2 =",zahl1+zahl2)
print("Zahl 2 - Zahl 1 =",zahl2-zahl1)
print("Zahl 1 * Zahl 2 =",zahl1*zahl2)
print("Zahl 2 / Zahl 1 =",zahl2/zahl1)

# Aufgabe 1

aufgabe1_1 = "Heute haben wir das Terminal geöffnet, Python mit Befehlen geupdated und erste Erfahrungen mit Befehlen gesammelt wie z.B. Print, Float, INT etc."
aufgabe1_2 = "In meinem wiki habe ich Vergleichsoperatoren hinzugefügt, die ich in Zukunft sicher oft gebrauchen werde"

# Aufgabe 2

note1 = int(float(input("gib die erste Note ein: ")))
note2 = int(float(input("gib die zweite ein: ")))
note3 = int(float(input("gib die dritte Note ein: ")))

# Berechnung des Durchschnitts
durchschnitt=(note1 + note2 + note3) / 3

# gibt das Ergebnis wieder
print("der Durchschnitt der Noten beträgt :",durchschnitt)

name = input("what is your name?: ")
print("Hello "+name)

age = input("how old are you?: ")
print("your age: "+age)

# input erlaubt es mir ein Eingabefeld zu erstellen, welches im Script auf eine Eingabe von mir erwartet, bevor das script weiter läuft
x = input("gib dein Alter an: ")
# int steht für Integer und erlaubt es mir str (strings/texte) in Zahlen umzuwandeln
a = int (x)
y = input("gib Marcus Alter an: ")
b = int (y)

print("Euer gemeinsames Alter beträgt: ", a+b)