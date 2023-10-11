from flask import Flask, redirect, url_for

from . import posts

def make_app(secret_key: str) -> Flask:
    app = Flask(__name__)

    app.secret_key = secret_key

    posts.init(app)

    @app.route('/')
    def index() -> str:
        return redirect(url_for('posts.index'))

    return app
