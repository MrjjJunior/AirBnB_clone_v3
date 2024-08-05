#!/usr/bin/python3
''' Creating a Flask application '''
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)


if __name__ == "__main__":
    HOST = getenv()
    PORT = int(getenv())
    app.run(hosts=HOST, port=PORT, threaded=True)