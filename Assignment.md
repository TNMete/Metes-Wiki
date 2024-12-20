# Aufgaben für den Nachmittag: Python-Code in Arbeitsschritte beschreiben

**Abgabe**: Text ()

## Aufgabe 1: Einfache Entscheidungen mit `if`-Statements (25 Punkte)

**Ziel:** Verstehen, wie Entscheidungen im Code in Arbeitsschritte übersetzt werden können.

Code-Beispiel:

```python
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 10:
    print("Die Zahl ist größer als 10.")
else:
    print("Die Zahl ist 10 oder kleiner.")
```

- Schreibe die Arbeitsschritte auf:

 In diesem Code wird der Benutzer aufgefordert eine Zahl im Integerformat einzugeben, welcher dann überprüft wird ob die eingegebene Zahl größer oder kleiner als 10 ist.

---

## Aufgabe 2: Listen verstehen und mit Python erstellen (20 Punkte)

**Ziel:** Verstehen, wie Datenstrukturen wie Listen verwendet werden können.

Code-Beispiel:

```python
zahlen = [1, 2, 3, 4, 5]
print("Die erste Zahl ist:", zahlen[0])
print("Die letzte Zahl ist:", zahlen[-1])
```

- Schreibe die Arbeitsschritte auf:

In dieser Aufgabe wird erst in einem Array festgelegt welche Zahlen mit der Funktion "zahlen" wiedergegeben werden sollen. Durch die "0" in Klammern wird erst von links nach rechts gelesen und mit der "-1" von rechts nach links.

**Zusatzaufgabe:** Erstelle selbst eine Liste mit Wochentagen und schreibe die Arbeitsschritte auf.

zahlen = [Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag]
print("Die erste Zahl ist:", zahlen[0])
print("Die letzte Zahl ist:", zahlen[-1])

---

## Aufgabe 3: Entscheidungslogik erweitern (25 Punkte)

**Ziel:** Die Funktionsweise von mehreren Bedingungen in Python verstehen und in Arbeitsschritte übertragen.

Code-Beispiel:

```python
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 0:
    print("Die Zahl ist positiv.")
elif zahl < 0:
    print("Die Zahl ist negativ.")
else:
    print("Die Zahl ist null.")
```

- Schreibe die Arbeitsschritte auf:

In diesem Code wird der Benutzer aufgefordert eine Zahl im Integerformat einzugeben und anschließend wird diese Zahl mit einer if und elif Funktion überpürft ob sie positiv oder negativ ist. Wenn es weder positiv oder negativ ist, wird es durch die else Funktion ausgegeben das die Zahl "0" ist.

---

## Aufgabe 4: Funktionen verstehen (20 Punkte)

**Ziel:** Lernen, wie Funktionen in Python definiert werden und was in jedem Arbeitsschritt passiert.

Code-Beispiel:

```python
def ist_gerade(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False

zahl = int(input("Gib eine Zahl ein: "))
if ist_gerade(zahl):
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")
```

- Schreibe die Arbeitsschritte auf

Zweck der Funktion "ist_gerade" prüft, ob eine Zahl gerade ist, und gibt entsprechend True oder False zurück.
Wie bei Aufgabe 3 wird der Benutzer aufgefordert eine Zahl einzugeben und diese wird durch "if" und "else" überpürft ob sie gerade oder ungerade ist.
In diesem Fall ist kein "elif" nötig, weil es nur 2 Optionen gibt (gerade oder ugnerade).

---

## Aufgabe 5: Benutzerinteraktion (10 Punkte)

**Ziel:** Die Struktur eines Programms mit Benutzereingaben und Ausgaben analysieren.

Code-Beispiel:

```python
name = input("Wie heißt du? ")
alter = int(input("Wie alt bist du? "))
print(f"Hallo {name}, in 10 Jahren wirst du {alter + 10} Jahre alt sein!")
```

- Schreibe die Arbeitsschritte auf.

1. Input erfragt die variable "name" vom Benutzer

2. Input erfragt mit "int" das "Alter" vom Benutzer

3. print gibt nun einen mit f formatierten string aus der die Variable "name" und die Variable "alter" mit 10 addiert.

---

Diese Aufgaben sind auf den bisherigen Stand der Vorlesung abgestimmt und bieten eine gute Balance zwischen Verständnis und Anwendung. Punkte sind proportional zur Komplexität der Aufgabe verteilt.
