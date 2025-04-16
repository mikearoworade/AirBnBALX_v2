#!/usr/bin/python3
""" Starts a simple Flask web application """
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    return "Hello World!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return "C {}".format(text.replace("_", " "))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    return "Python {}".format(text.replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('number.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    parity = "even" if n % 2 == 0 else "odd"
    return render_template('number_odd_or_even.html', number=n, parity=parity)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
