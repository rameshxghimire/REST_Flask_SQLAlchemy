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


# Inventory Item Class
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(250))
    available = db.Column(db.Integer)
    last_ordered = db.Column(db.Text)

    def __init__(self, name, description, available, last_ordered):
        self.name = name
        self.description = description
        self.available = available
        self.last_ordered = last_ordered


# Create the schema
class ItemSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "available", "last_ordered")


# Initialise the schema
item_schema = ItemSchema(strict = True)
items_schema = ItemSchema(many=True, strict=True)



if __name__ == "__main__":
    app.run(debug=True)  # debug set to True for dev env

# todo: add vendors
# todo: add authentication