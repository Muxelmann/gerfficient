from flask import Flask


def make_app(secret_key: str) -> Flask:
    app = Flask(__name__)

    app.secret_key = secret_key

    @app.route('/')
    def index() -> str:
        return "Hello, world!"

    return app
