#!/usr/bin/python3
"""
Flask web application listening on 0.0.0.0, port 5000
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the
text variable (replace underscore _
/number/<n>: display “n is a number” only if n is an integer
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    method that returns arg passed
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    method that returns arg passed
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    this route definition uses the defaults keyword
    argument to specify a default value of "is cool"
    return 'Python {}'.format(text.replace('_', ' '))
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """
    displays an int
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
