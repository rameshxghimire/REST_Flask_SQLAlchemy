""" app.py the main application file. """

# imports
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Initialise the app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# setup the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "db.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialise the database
db = SQLAlchemy(app)

# initialise the marshmallow
ma = Marshmallow(app)


if __name__ == "__main__":
    app.run(debug=True)  # debug set to True for dev env

# todo: add vendors
# todo: add authentication