import os
import hmac
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.environ["API_KEY"]

@app.route("/")
def home():
    return jsonify(message="Welcome to my API!")

@app.route("/hello")
def hello():
    provided_key = request.headers.get("X-API-Key", "")

    if not hmac.compare_digest(provided_key, API_KEY):
        return jsonify(error="Unauthorized"), 401

    return jsonify(message="Hello, World!")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )