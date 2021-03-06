#!/usr/bin/python3
'''Starts a flask application'''
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    '''Print a text'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    '''Print a text in hbnb directory'''
    return "HBNB"


@app.route('/c/<text>')
def print_c(text):
    '''Print c with a directory'''
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python')
@app.route('/python/<text>')
def print_python(text=None):
    '''Print python with a directory or just python if there is dir'''
    if text is None:
        return "Python is cool"
    else:
        text = text.replace('_', ' ')
        return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
