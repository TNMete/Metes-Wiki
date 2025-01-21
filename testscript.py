# rezepte = {
#     "Spiegelei": "Zutaten: Ei, Salz, Paprika & Pfeffer.",
#     "Salat": "Zutaten: Blattsalat, Tomaten, Gurken, Dressing.",
# }


# def zeige_rezepte():
#     print("Verfügbare Rezepte:")
#     rezept_liste = list(rezepte.keys())

#     for i, rezept in enumerate(rezept_liste, start=1):
#         print(f"{i}. {rezept}")

#     # Auswahl
#     try:
#         auswahl = int(input("Bitte die Nummer des Rezepts eingeben: ")) - 1
#         if 0 <= auswahl < len(rezept_liste):
#             rezept_name = rezept_liste[auswahl]
#             print(f"\nRezept für {rezept_name}:")
#             print(rezepte[rezept_name])
#         else:
#             print("Ungültige Auswahl. Bitte eine Nummer aus der Liste wählen.")
#     except ValueError:
#         print("Bitte eine gültige Zahl eingeben.")


# zeige_rezepte()


# NEUER TEST:

# zahlen = [45, 23, 666, 124551, 5, 6, 7, 8, 9]


# def verarbeite_liste(zahlen):
#     summe = sum(zahlen)

#     ungerade_zahlen = [zahl for zahl in zahlen if zahl % 2 != 0]

#     groesste_zahl = max(zahlen)

#     print("Summe der Zahlen:", summe)
#     print("Ungerade Zahlen:", ungerade_zahlen)
#     print("Größte Zahl in der Liste:", groesste_zahl)


# verarbeite_liste(zahlen)


# import socket

# hostname = "example.com"
# ip_address = socket.gethostbyname(hostname)
# print(f"Die IP-Adresse von {hostname} ist {ip_address}")

# --------------------------------------------------------------------------

# import os
# import platform

# host = input("gib deinen host ein: ")


# def ping(host):
#     param = "-n" if platform.system().lower() == "windows" else "-c"
#     command = f"ping {param} 4 {host}"
#     return os.system(command)


# # host = "google.com"
# ping(host)

# --------------------------------------------------------------------------

# import ipaddress

# network = ipaddress.ip_network("192.168.10.0/24")
# print(f"Netzwerk: {network}")
# print(f"Erste IP: {network[0]}")
# print(f"Letzte IP: {network[-1]}")
# print(f"Anzahl nutzbarer Hosts: {network.num_addresses - 2}")

# --------------------------------------------------------------------------


# ---------------------------------------------------------

from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Welcome Mamazon"


@app.route("/item/<product_id>", methods=["GET"])
def get_item(product_id):
    color = request.args.get("color")  # /item/2?color=black
    size = request.args.get("size")  # /item/2?size=M
    # /item/2?color=black&size=M
    return f"Welcome Mamazon's item {product_id} with the color {color} an with the size {size}"


@app.route("/brand", methods=["GET"])
def get_mamazon_default_brand_page():
    # Should return a welcome to brand page text
    return "Welcome to brand page"


@app.route("/brand/<brand_id>", methods=["GET"])
def get_brand_by_id(brand_id):
    # Should return  welcome to specific brand page text
    # E.g. Welcome to Hilfigher (dynamisch)
    # Should be able to filter by brand type and should display the filter on the screen

    clothing_type = request.args.get("type")
    # E.g. Welcome to Hilfigher and the type is t-shirts
    # Should be able to filter by condition of the article and should display the condition on the screen
    # --> Goals E.g. Welcome to Hilfigher and the type is t-shirts and the condition is used
    condition = request.args.get("condition")
    color = request.args.get("color")
    return f"The brand name is:{brand_id}, type: {clothing_type} and has the condition: {condition} with the color: {color}."


# http://localhost:6060/brand/Hilfigher?type=t-shirt&condition=brand+new

if __name__ == "__main__":
    app.run(debug=True, port=6060)
