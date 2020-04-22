#!/usr/bin/python3
'''Starts a flask application'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def remove_SQLAlchemy_session(self):
    '''remove SQLAlchemy session'''
    storage.close()


@app.route('/hbnb_filters')
def filters():
    '''displays (html page) 6-index.html'''
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
