#!/usr/bin/python3
""" Index of the route """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    ''' Returns a JSON file with "status": "OK" '''
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ endpoint that retrieves the number of each objects by type """
    classes = {"Amenity": "amenities", "City": "cities",
               "Place": "places", "Review": "reviews",
               "State": "states", "User": "users"}
    stats_dict = {}
    for cls in classes.keys():
        stats_dict[classes[cls]] = storage.count(cls)
    return jsonify(stats_dict)
