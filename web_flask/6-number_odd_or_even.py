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

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home() -> str:
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb() -> str:
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def func_text(text: str) -> str:
    return "C {0}".format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def func_python_text(text="is cool") -> str:
    return "Python {0}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_is_number(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def render_is_odd(n):
    what_is = None

    if n % 2 == 0:
        what_is = "even"
    else:
        what_is = "odd"

    return render_template('6-number_odd_or_even.html', n=n, type_data=what_is)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
