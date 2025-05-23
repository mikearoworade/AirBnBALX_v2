#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.review import Review

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """Close storage session after each request"""
    storage.close()

@app.route('/hbnb')
def hbnb():
    """Display the HBNB page"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    places = sorted(storage.all(Place).values(), key=lambda x: x.name)
    try:
        user_objs = storage.all(User)
        users = {user.id: user for user in user_objs.values()}
    except Exception as e:
        users = {}
        print(f"Error loading users: {e}")
    reviews = storage.all(Review)


    return render_template(
        'hbnb.html',
        states=states,
        amenities=amenities,
        places=places,
        users=users,
        reviews=reviews
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
