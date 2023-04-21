#!/usr/bin/python3
"""
Flask web application listening on 0.0.0.0, port 5000
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the
text variable (replace underscore _
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
