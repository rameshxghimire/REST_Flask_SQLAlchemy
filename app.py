""" app.py the main application file. """

# imports
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Initialise the app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

if __name__ == "__main__":
    app.run(debug=True)  # debug set to True for dev env

# todo: add vendors
# todo: add authentication