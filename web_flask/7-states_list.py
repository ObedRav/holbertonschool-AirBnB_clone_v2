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
import models

app = Flask(__name__)


@app.route('/states_list')
def states_list():
    states = models.storage.all(models.State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear(self):
    models.storage.close()


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
