#!/usr/bin/env bash
""" Index of the route """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    ''' Returns a JSON file with "status": "OK" '''
    return jsonify({"status": "OK"})
