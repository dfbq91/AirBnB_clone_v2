#!/usr/bin/python3
'''Starts a flask application'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    '''Print a text'''
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
