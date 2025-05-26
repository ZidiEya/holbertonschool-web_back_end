#!/usr/bin/env python3
""" Index view """
from flask import jsonify, abort
from api.v1.views import app_views

@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized():
    """ GET /api/v1/unauthorized triggers 401 error """
    abort(401)
