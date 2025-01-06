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
