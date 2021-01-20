#!/usr/bin/python3
""" Starts a Flask web-app """
from flask import Flask
web_app = Flask(__name__)


@web_app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Shows Hello HBNB """
    return 'Hello HBNB!'


@web_app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Shows HBNB """
    return 'HBNB!'


@web_app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Shows C + text """
    return 'C {}'.format(text.replace('_', ' '))


@web_app.route('/python/', strict_slashes=False)
@web_app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """ Shows Python + text """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)
