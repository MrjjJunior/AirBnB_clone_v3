#!/usr/bin/python3
''' Flask application '''
from apiv1.views import app_views
from Flask import flask
from models import storage

app = Flask(__name__)


@app.route('/')
def app_views():
    pass


if __name__ == "__main__":
    app.run(debug=True)
