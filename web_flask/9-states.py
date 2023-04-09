#!/usr/bin/python3
"""
Module Name:
1-hbnb_route

Module Description:
This module contains the routers

Module Attributes:
- None
"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_list_id(id):
    states = storage.all(State).values()

    state = None

    for current_state in states:
        if current_state.id == id:
            state = current_state

    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def tear(self):
    storage.close()


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
