#!/usr/bin/env python3
"""Flask app for API V1"""
import os
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from api.v1.auth.basic_auth import BasicAuth

app = Flask(__name__, static_url_path='')
app.register_blueprint(app_views)
auth = None

# Initialize authentication based on environment
if os.getenv('AUTH_TYPE') == 'basic_auth':
    auth = BasicAuth()

@app.before_request
def before_request():
    """Enforce authentication and attach current_user to request."""
    if auth is None:
        return

    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if not auth.require_auth(request.path, excluded_paths):
        return

    # Missing credentials → 401
    if auth.authorization_header(request) is None:
        abort(401)
    # Invalid credentials → 403
    user = auth.current_user(request)
    if user is None:
        abort(403)
    # Attach for downstream handlers
    request.current_user = user

@app.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    """Health check endpoint."""
    return jsonify({'status': 'OK'})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'error': 'Unauthorized'}), 401

@app.errorhandler(403)
def forbidden(error):
    return jsonify({'error': 'Forbidden'}), 403

if __name__ == '__main__':
    host = os.getenv('API_HOST', '0.0.0.0')
    port = int(os.getenv('API_PORT', 5000))
    app.run(host=host, port=port)
