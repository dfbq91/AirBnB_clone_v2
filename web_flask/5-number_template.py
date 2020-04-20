#!/usr/bin/python3
'''Starts a flask application'''
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    '''Prints a text'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    '''Prints a text in hbnb directory'''
    return "HBNB"


@app.route('/c/<text>')
def print_c(text):
    '''Prints c with a directory'''
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python')
@app.route('/python/<text>')
def print_python(text=None):
    '''Prints python with a directory or just python if there is dir'''
    if text is None:
        return "Python is cool"
    else:
        text = text.replace('_', ' ')
        return "Python {}".format(text)


@app.route('/number/<int:n>')
def print_number(n):
    '''prints if n is an int number'''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def display_template(n=None):
    '''displays a html page if n is an int'''
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
