"""A tiny greeting API used to test Antilog cloud sessions end to end."""

import os

from flask import Flask, jsonify, request


def create_app() -> Flask:
    app = Flask(__name__)
    greeting = os.environ.get("GREETING")
    if not greeting:
        raise RuntimeError("GREETING is not set: copy .env.example and set it, or set it in the environment")

    @app.get("/health")
    def health():
        return jsonify(ok=True)

    @app.get("/hello")
    def hello():
        name = request.args.get("name", "world").strip() or "world"
        return jsonify(message=f"{greeting}, {name}!")

    return app
