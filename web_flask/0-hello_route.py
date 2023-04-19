#!/usr/bin/python3
"""
Module contains the bash script that prints hello HBNB
"""
from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Route for the root URL
@app.route('/', strict_slashes=False)
def hello():
    """function that contains the flask command"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    # Run the app on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
