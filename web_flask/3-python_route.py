from flask import Flask

# Create a Flask app
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """function that contains the flask command"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """function that returns hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """function that returns hbnb"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/(<text>)', strict_slashes=False)
def python_text(text):
    """function that returns hbnb"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    # Run the app on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)

