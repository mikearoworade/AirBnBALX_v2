#!/usr/bin/python3
"""Flask app to display cities by states."""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception=None):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with cities by states."""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
