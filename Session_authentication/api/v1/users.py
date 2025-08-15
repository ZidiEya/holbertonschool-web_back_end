#!/usr/bin/env python3
"""Users view"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.user import User

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """
    Retrieve a User object by id or 'me' for current authenticated user
    """
    if user_id == "me":
        if not request.current_user:
            abort(404)
        return jsonify(request.current_user.to_dict())

    user = User.get(user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())
