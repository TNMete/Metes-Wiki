def begruessung(name):
    print("Hallo, " + name)


def addiere_zahlen(a, b):
    ergebnis = a + b
    return ergebnis


def subtrahiere_zahlen(a, b):
    return a - b


def main():
    zahl1 = int(input("Gib eine Zahl ein: "))
    zahl2 = int(input("Gib eine weitere Zahl ein: "))

    summe = addiere_zahlen(zahl1, zahl2)
    print("Die Summe ist: " + str(summe))

    differenz = subtrahiere_zahlen(zahl1, zahl2)
    print("Die Differenz ist: " + str(differenz))

    begruessung("Max")


if __name__ == "__main__":
    main()
