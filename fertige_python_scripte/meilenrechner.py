# Zusatzaufgabe - Meilenrechner

a = input("Geben Sie die Kilometer ein, die in Meilen umgerechnet werden sollen: ")

def km_in_meilen(km):
    x = float(km)
    c = float(0.621371)
    d = x * c
    return d

print (a, "Kilometer entsprechen:", km_in_meilen(a), "Meilen")