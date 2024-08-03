#!/usr/bin/python3
''' Returns status response '''
from api.v1.views import app_views

@app.route('/status', method=['GET'])
def get_status():
    ''' return response status of api '''
    statuses = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
            }
    return jsonify(statuses)
