first_name = "Mete"
last_name = "Karaoglan"
age = "34"

zahl1 = 2
zahl2 = 10

# print gibt wieder was im Befehl steht
print(first_name + " " + last_name + " " + age)

print("Zahl 1 + Zahl 2 =",zahl1+zahl2)
print("Zahl 2 - Zahl 1 =",zahl2-zahl1)
print("Zahl 1 * Zahl 2 =",zahl1*zahl2)
print("Zahl 2 / Zahl 1 =",zahl2/zahl1)

# meine Noten
note1 = 2
note2 = 5
note3 = 3

# Berechnung des Durchschnitts
durchschnitt=(note1 + note2 + note3) / 3
print("der Durchschnitt deiner Noten beträgt :",durchschnitt)

name = input("What is your name?: ")
print("Hello "+name)

age = input("how old are you?: ")
print("Your age: "+age)

# input erlaubt es mir ein Eingabefeld zu erstellen, welches im Script auf eine Eingabe von mir erwartet, bevor das script weiter läuft
x = input("Gib dein Alter an: ")
# int steht für Integer und erlaubt es mir str (strings/texte) in Zahlen umzuwandeln
a = int (x)
y = input("Gib Marcus Alter an: ")
b = int (y)

print("Euer gemeinsames Alter beträgt: ", a+b)