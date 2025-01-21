from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/brand/<int:brand_id>", methods=["GET"])
def get_brand_by_id(brand_id):
    brand_type = request.args.get("type")
    brand_condition = request.args.get("condition")
    return f"Brand-ID {brand_id},  Type: {brand_type}, Condition: {brand_condition}."


@app.route("/product/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    return f"Product-ID: {product_id}"


@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    return f"Searching for: {query}"


@app.errorhandler(400)
def invalid_usage(error):
    return jsonify({"error": "Ungültige ID, muss eine Zahl sein."}), 400


if __name__ == "__main__":
    app.run(debug=True, port=6060)
