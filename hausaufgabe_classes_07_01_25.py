# class Auto:
#     def __init__(self, marke):
#         self.marke = marke

#     def beschreibung(self):
#         return f"Dies ist ein Auto der Marke {self.marke}."


# mein_auto = Auto("BMW")
# print(mein_auto.beschreibung())  # Ausgabe: Dies ist ein BMW Auto.


class Rechner:
    def addiere(self, a, b):
        return a + b


mein_rechner = Rechner()
print(mein_rechner.addiere(5, 3))


# --------------------------------------------------------

# class Server:
#     def __init__(self, name, ip, standort):
#         self.name = name
#         self.ip = ip
#         self.standort = standort


# def boot(self):
#     print(f"Der Server {self.name} mit der IP {self.ip} wird hochgefahren.")


# def shutdown(self):
#     print(f"Der Server am {self.standort} wird heruntergefahren.")


# my_server = Server("Server1", "192.168.0.1.", "Frankfurt")
# print(my_server.name)

# my_server.programs = ["Google"]
# print(my_server.programs)

# --------------------------------------------------------


# class Auto:
#     def __init__(self, marke, reichweite, motor, kilometer):
#         self.marke = marke
#         self.restreichweite = reichweite
#         self.motor = motor
#         self.kilometerzahl = kilometer


# def fahren(self, km):
#     self.kilometerzahl += km
#     self.restreichweite -= km


# def tanken(self, km):
#     self.restreichweite += km


# def fahren(self):
#     print(float(f"Das Auto der Marke {self.marke} faehrt {self.kilometerzahl}."))


# def tanken(self):
#     print(float(f"Das Auto muss nach {self.reichweite} tanken."))

# ------------------------[Aufgabe 1]------------------------------


class Zutat:
    def __init__(self, name, kalorien_pro_100g, zubereitungszeit):
        self.name = name
        self.kalorien_pro_100g = kalorien_pro_100g
        self.zubereitungszeit = zubereitungszeit


# ------------------------[Aufgabe 1.2]------------------------------


class Rezept:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung
        self.zutatenliste = {}

    def zutat_hinzufügen(self, Zutat, Menge):
        self.zutatenliste[Zutat] = Menge

    # def kalorien(self, ):

    # def kochzeit(self, ):

    # def rezept_anzeigen(self, ):


test = Rezept("Leckerer", "Pfannkuchen")
print(test.beschreibung)
