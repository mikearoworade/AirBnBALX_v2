#!/usr/bin/python3
"""Flask app for HBNB filters route"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes SQLAlchemy session or file storage"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays states and amenities for filtering"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda a: a.name)
    return render_template('hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
