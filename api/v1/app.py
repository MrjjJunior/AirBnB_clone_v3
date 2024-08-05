#!/usr/bin/python3
''' Creating a Flask application '''
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    ''' closes database storage '''
    storage.close()

@app.errorhandler(404)
def not_found(error):
    ''' 404 error response '''
    retrun make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    HOST = getenv()
    PORT = int(getenv())
    app.run(hosts=HOST, port=PORT, threaded=True)