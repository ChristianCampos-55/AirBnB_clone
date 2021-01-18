#!/usr/bin/python3
""" Starts a Flask web-app """
from flask import Flask
web_app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Shows Hello HBNB """
    return 'Hello HBNB!'


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)
