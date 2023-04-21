from flask import Flask
"""
Flask web application listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    method that returns the arg passed
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    method that returns the arg passed
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)