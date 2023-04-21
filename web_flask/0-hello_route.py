from flask import Flask
"""
script that starts a Flask web application listening on port
0.0.0.0 port 5000
"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    method that prints to the browser any returned arg
    """
    return "Hello HBnB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
