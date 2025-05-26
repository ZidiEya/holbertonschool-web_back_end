#!/usr/bin/env python3

from flask import jsonify

@app.errorhandler(401)
def unauthorized_error(error):
    """ 401 Unauthorized error handler """
    return jsonify({"error": "Unauthorized"}), 401
