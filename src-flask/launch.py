import os
from gerfficient import make_app

secret_key = os.environ.get("FLASK_SECRET", None)
if secret_key is None:
    raise Exception("Specify a valid `FLASK_SECRET`")

app = make_app(secret_key)