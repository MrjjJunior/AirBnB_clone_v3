#!/usr/bin/python3
''' Creating a Flask application '''
from flask import Flask, render_template, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    ''' closes database storage '''
    storage.close()

@app.errorhandler(404)
def not_found(error):
    ''' 404 error response '''
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=HOST, port=PORT, threaded=True)