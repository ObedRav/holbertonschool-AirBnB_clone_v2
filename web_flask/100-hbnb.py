#!/usr/bin/python3
"""
Module Name:
10-hbnb_filters

Module Description:
This module contains the routers

Module Attributes:
- None
"""
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models import storage

app = Flask(__name__)


@app.route('/hbnb')
def states_list():
    """
    This endpoint renders an HTML page that displays a list of
    states and amenities retrieved from a database.
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template(
        '100-hbnb.html',
        states=states,
        amenities=amenities,
        places=places
    )


@app.teardown_appcontext
def tear(self):
    """Tear"""
    storage.close()


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
