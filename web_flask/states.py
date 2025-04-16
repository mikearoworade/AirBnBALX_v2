#!/usr/bin/python3
"""Flask app that displays states and their cities"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception=None):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Display list of states or a specific state with its cities."""
    states = storage.all(State)
    if id:
        state = states.get("State.{}".format(id))
        if state:
            cities = sorted(state.cities, key=lambda c: c.name)
            return render_template('states.html', state=state, cities=cities)
        else:
            return render_template('states.html', not_found=True)
    else:
        sorted_states = sorted(states.values(), key=lambda s: s.name)
        return render_template('states.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
