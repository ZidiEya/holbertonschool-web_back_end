# api/v1/app.py

from flask import Flask, jsonify, abort, request
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
import os

# ... existing code ...

@app.before_request
def before_request():
    if auth is None:
        return
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if not auth.require_auth(request.path, excluded_paths):
        return
    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)
    request.current_user = auth.current_user(request)  # ✅ assign current user
