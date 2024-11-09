from flask import Flask, jsonify, request
from handler import get_user_data

app = Flask(__name__)

@app.route('/users/<int:user_id>', methods=['GET'])
def user_data(user_id):
    data = get_user_data(user_id)
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Service unavailable"}), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
