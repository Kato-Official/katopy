from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Katopy!"})

@app.route("/greet", methods=["POST"])
def greet():
    data = request.get_json()
    name = data.get("name", "friend")
    return jsonify({"greeting": f"Hello, {name}!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
