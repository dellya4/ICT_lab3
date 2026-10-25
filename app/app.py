import socket

from datetime import datetime
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True)

    if not data or "message" not in data:
        return jsonify({
            "error": "field 'message' is required"
        }), 400

    if not isinstance(data["message"], str):
        return jsonify({
            "error": "field 'message' must be a string"
        }), 400

    return jsonify({
        "reply": data["message"]
    }), 200


@app.route("/time", methods=["GET"])
def get_time():
    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    return jsonify({
        "time": current_time,
        "served_by": socket.gethostname()
    }), 200


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "resource not found"
    }), 404


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )