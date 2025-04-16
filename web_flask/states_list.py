#!/usr/bin/python3
"""Flask web application to display states from storage"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Remove current SQLAlchemy Session after each request"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a HTML page with a list of all State objects sorted by name"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('states_list.html', states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
