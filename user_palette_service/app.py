from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

users = {}  # In-memory data storage for users
palettes = {}  # In-memory data storage for palettes

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "running"}), 200

@app.route("/users/register", methods=["POST"])
def register_user():
    user_data = request.json
    user_id = len(users) + 1
    users[user_id] = user_data
    return jsonify({"user_id": user_id, "user_data": user_data}), 201

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/palettes", methods=["POST"])
def create_palette():
    palette_data = request.json
    palette_id = len(palettes) + 1
    palettes[palette_id] = palette_data
    return jsonify({"palette_id": palette_id, "palette_data": palette_data}), 201

def register_service():
    register_url = os.getenv("REGISTER_URL")
    service_info = {
        "service_name": "user-palette-service",
        "instance_url": "http://user-palette-service:5000"
    }
    requests.post(register_url, json=service_info)

if __name__ == "__main__":
    register_service()
    app.run(host="0.0.0.0", port=5000)
