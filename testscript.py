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

# from flask import Flask, request

# app = Flask(__name__)


# @app.route("/", methods=["GET"])
# def home():
#     return "Welcome Mamazon"


# @app.route("/item/<product_id>", methods=["GET"])
# def get_item(product_id):
#     color = request.args.get("color")  # /item/2?color=black
#     size = request.args.get("size")  # /item/2?size=M
#     # /item/2?color=black&size=M
#     return f"Welcome Mamazon's item {product_id} with the color {color} an with the size {size}"


# @app.route("/brand", methods=["GET"])
# def get_mamazon_default_brand_page():
#     # Should return a welcome to brand page text
#     return "Welcome to brand page"


# @app.route("/brand/<brand_id>", methods=["GET"])
# def get_brand_by_id(brand_id):
#     # Should return  welcome to specific brand page text
#     # E.g. Welcome to Hilfigher (dynamisch)
#     # Should be able to filter by brand type and should display the filter on the screen

#     clothing_type = request.args.get("type")
#     # E.g. Welcome to Hilfigher and the type is t-shirts
#     # Should be able to filter by condition of the article and should display the condition on the screen
#     # --> Goals E.g. Welcome to Hilfigher and the type is t-shirts and the condition is used
#     condition = request.args.get("condition")
#     color = request.args.get("color")
#     return f"The brand name is:{brand_id}, type: {clothing_type} and has the condition: {condition} with the color: {color}."


# # http://localhost:6060/brand/Hilfigher?type=t-shirt&condition=brand+new

# if __name__ == "__main__":
#     app.run(debug=True, port=6060)

# ------------------------------------------------------------------
# from flask import Flask, request
# from testscript_users import users

# app = Flask(__name__)


# @app.route("/users/<int:user_id>", methods=["GET"])
# def get_user_by_id(user_id):
#     final_user = None

#     for u in users:
#         if u["id"] == user_id:
#             final_user = u

#     if final_user == None:
#         return "User could not be found "

#     return f"The User is {final_user}"


# # Route 3: /search?name=<name>
# # Beispiel: http://localhost:6060/search?name=Charlie
# # Rückgabe: "Found user: Charlie" oder "No user found with name: Charlie"
# @app.route("/search", methods=["GET"])
# def get_user_by_name():
#     final_user = None
#     name = request.args.get("name")
#     for u in users:
#         if u["firstName"] == name:
#             final_user = u

#     if final_user == None:
#         return "User could not be found"

#     return f"The User is {final_user}"


# # 1. Postman installieren
# # 2. url eingeben, POST Befehl aushwählen --> siehe Screenshot
# # 3. Ausführen und veschiedene Parameter im  body angeben
# # 4. Zusatz: Versuchen den richtigen Benutzer zu bekommen
# # 5. Zusatz Zusatz: Versucht eine weitere post anfrage mit signup zu erstellen,
# # welche Route einen neuen Nutzer in die Liste einfügt
# @app.route("/users/login", methods=["POST"])
# def login():
#     credentials = request.get_json()
#     username = credentials["username"]
#     password = credentials["password"]
#     # Now you can access the user based on email and password and return if valid credentials
#     return f"Hallo {credentials} {username} {password}"


# if __name__ == "__main__":
#     app.run(debug=True, port=6060)

# ---------------------------------------------------

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-Memory "Datenbank"
products = []


# POST - fügt ein neues Produkt hinzu
# definiert URL und Methode
@app.route("/products", methods=["POST"])
# definiert die auszuführende Funktion
def create_product():
    # übersetzt java script object in ein python dictinoary
    new_product = request.get_json()
    # Validierungen - sind alle Daten vorhanden?
    if not new_product or "name" not in new_product or "price" not in new_product:
        # ungültige Anfrage: return error
        return (
            jsonify({"error": "Invalid input"}),
            400,
        )

    new_product["id"] = (
        # generiert ID's für die eingegebenen Produkte
        max([produkt["id"] for produkt in products], default=0)
        + 1
    )
    # fügt der Liste hinzu
    products.append(new_product)
    # return 201 heißt Eingabe wurde erfolgreich erstellt und gibt Produkt aus
    return (
        jsonify(new_product),
        201,
    )


# GET - Alle Produkte abrufen
# definiert URL und Methode
@app.route("/products", methods=["GET"])
# definiert die auszuführende Funktion
def get_products():
    # "name" wird aus requests abgerufen
    name_filter = request.args.get("name")
    print(name_filter)
    # validiert ob name existiert
    if name_filter:
        # 1. falls Übereinstimmung, speichert in "filtered_products"
        # 2. loop über Produkte
        # 3. prüft ob der eingegebene Name mit dem Produktnamen übereinstimmt
        filtered_products = [
            p for p in products if name_filter.lower() in p["name"].lower()
        ]
        # Liste der gefilterten Produkte werden ausgegeben
        return jsonify(filtered_products), 200
    return jsonify(products), 200


if __name__ == "__main__":
    app.run(debug=True, port=6060)
