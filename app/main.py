from flask import Flask, jsonify, request

app = Flask(__name__)

products = []

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify({
        "status": "success",
        "data": products
    })

@app.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()

    new_product = {
        "id": len(products) + 1,
        "name": data.get("name"),
        "price": data.get("price")
    }

    products.append(new_product)

    return jsonify({
        "status": "success",
        "data": new_product
    })

@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    for product in products:
        if product["id"] == id:
            return jsonify({
                "status": "success",
                "data": product
            })

    return jsonify({
        "status": "error",
        "message": "Product not found"
    }), 404

@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.get_json()

    for product in products:
        if product["id"] == id:
            product["name"] = data.get("name", product["name"])
            product["price"] = data.get("price", product["price"])

            return jsonify({
                "status": "success",
                "data": product
            })

    return jsonify({
        "status": "error",
        "message": "Product not found"
    }), 404

@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    for product in products:
        if product["id"] == id:
            products.remove(product)
            return jsonify({
                "status": "success",
                "message": "Product deleted"
            })

    return jsonify({
        "status": "error",
        "message": "Product not found"
    }), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)