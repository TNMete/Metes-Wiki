def calc_area(width, height):
    return width * height


breite = float(input("Gib die Breite des Rechtecks ein: "))
hoehe = float(input("Gib die Höhe des Rechtecks ein: "))

flaeche = calc_area(breite, hoehe)
print(f"Die Fläche des Rechtecks beträgt: {flaeche}")
