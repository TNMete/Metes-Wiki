def addition(zahl1, zahl2):
    return zahl1 + zahl2


def subtraktion(zahl1, zahl2):
    return zahl1 - zahl2


def multiplikation(zahl1, zahl2):
    return zahl1 * zahl2


def division(zahl1, zahl2):
    return zahl1 / zahl2


def calculator():

    choice = input("gib die gewünschten Operation ein (1/2/3/4): ")

    zahl1 = float(input("gib deine erste Zahl ein: "))
    zahl2 = float(input("gib deine zweite Zahl ein: "))

    if choice not in ["1", "2", "3", "4"]:
        print("Bitte versuche es erneut")
        return

    if choice == "1":
        print(addition(zahl1, zahl2))
    elif choice == "2":
        print(subtraktion(zahl1, zahl2))
    elif choice == "3":
        print(multiplikation(zahl1, zahl2))
    elif choice == "4":
        print(division(zahl1, zahl2))


print("Welche Operation möchtest du ausführen?")
print("1: addition")
print("2: subtraktion")
print("3: multiplikation")
print("4: division")

calculator()
