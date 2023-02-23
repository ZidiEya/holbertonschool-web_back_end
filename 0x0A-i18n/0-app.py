#!/usr/bin/env python3

"""Router module for the API
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """ GET /
    Return:
        Hello world
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
