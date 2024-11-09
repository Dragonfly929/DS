from flask import request, jsonify
import requests
from .load_balancer import LoadBalancer

load_balancer = LoadBalancer()

def setup_router(app):
    # Endpoint to register new services
    @app.route("/register", methods=["POST"])
    def register_service():
        data = request.json
        service_name = data.get("service_name")
        instance_url = data.get("instance_url")
        load_balancer.register_service(service_name, instance_url)
        return jsonify({"status": "registered"}), 200

    # Forward request to User and Palette Service
    @app.route("/users/<user_id>", methods=["GET"])
    def get_user(user_id):
        url = load_balancer.get_instance("user-palette-service")
        response = requests.get(f"{url}/users/{user_id}")
        return jsonify(response.json()), response.status_code

    # Forward request to Popularity Service
    @app.route("/palettes/<palette_id>", methods=["GET"])
    def get_palette(palette_id):
        url = load_balancer.get_instance("popularity-service")
        response = requests.get(f"{url}/palettes/{palette_id}")
        return jsonify(response.json()), response.status_code
