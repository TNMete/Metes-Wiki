# Zusatzaufgabe - Meilenrechner
def km_in_meilen(km):
    x = float(km)
    c = float(0.621371)
    d = x * c
    return d


a = input("Geben Sie die Kilometer ein, die in Meilen umgerechnet werden sollen: ")
print(a, "Kilometer entsprechen:", km_in_meilen(a), "Meilen")
