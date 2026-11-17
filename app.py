import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(service="Campus Tasks", status="ok")


@app.get("/health")
def health():
    status_code = int(os.environ.get("HEALTH_STATUS", "200"))
    return jsonify(service="Campus Tasks", status="healthy" if status_code == 200 else "unhealthy"), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
