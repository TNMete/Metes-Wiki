from flask import Flask, jsonify, request
from hausaufgabe_flask_users_21_01_25_a2 import users

app = Flask(__name__)


@app.route("/user/<int:id>", methods=["GET"])
def get_user(id):
    user = next((user for user in users if user["id"] == id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 400


@app.route("/login/<int:id>", methods=["GET"])
def login_user(id):
    user = next((user for user in users if user["id"] == id), None)
    if user:
        return jsonify({"message": f"User {user['name']} successfully logged in!"})
    else:
        return jsonify({"error": "User not found"}), 400


@app.route("/search", methods=["GET"])
def search_user():
    name = request.args.get("name")
    if name:
        user = next(
            (user for user in users if user["name"].lower() == name.lower()), None
        )
        if user:
            return jsonify({"message": f"Found user: {user['name']}"})
        else:
            return jsonify({"message": f"No user found with name: {name}"}), 400
    else:
        return jsonify({"error": "Name parameter is required"}), 400


if __name__ == "__main__":
    app.run(debug=True, port=6060)
