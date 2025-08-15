#!/usr/bin/env python3
"""Flask app entry point"""
from flask import Flask, jsonify, request
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.register_blueprint(app_views)

auth = None
if os.getenv("AUTH_TYPE") == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()

@app.before_request
def before_request():
    """Filter each request before processing"""
    if auth:
        request.current_user = auth.current_user(request)
