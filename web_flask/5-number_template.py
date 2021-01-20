#!/usr/bin/python3
""" Starts a Flask web-app """
from flask import Flask, render_template
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


@web_app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """ Prints passed number """
    return '{:d} is a number'.format(n)


@web_app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Displays html if num is an integer """
    return render_template('5-number.html', val=n)


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)
