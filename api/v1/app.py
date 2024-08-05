#!/usr/bin/python3
''' Flask application '''
from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    ''' Teardown of app context '''
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.00')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)