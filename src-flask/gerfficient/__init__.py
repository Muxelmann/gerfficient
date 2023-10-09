from flask import Flask

def make_app(secret_key: str) -> Flask:
    app = Flask(__name__)
    
    app.secret_key = secret_key

    return app