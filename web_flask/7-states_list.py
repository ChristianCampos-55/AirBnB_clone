#!/usr/bin/python3
""" Starts a Flask web-app """
from flask import Flask, render_template
from models.state import state
from models import storage
web_app = Flask(__name__)


@web_app.route('/states_list', strict_slashes=False)
def states_list():
    """ Lists states on HTML format """
    states_list = storage.all(State)
    states_list = states.values()
    return render_template('7-states_list.html', list_states=states_list)


@web_app.teardown_appcontext
def close_sess(exception):
    """ Close current session """
    storage.close()


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)
