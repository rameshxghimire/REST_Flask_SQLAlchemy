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


# API function: Create an item
@app.route("/item", methods=["POST"])
def add_item():
    name = request.json["name"]
    description = request.json["description"]
    available = request.json["available"]
    last_ordered = request.json["last_ordered"]

    new_item = Item(name, description, available, last_ordered)

    db.session.add(new_item)
    db.session.commit()

    return item_schema.jsonify(new_item)


# API function: Get all items
@app.route("/items", methods=["GET"])
def get_items():
    all_items = Item.query.all()
    result = items_schema.dump(all_items)
    return jsonify(result.data)


# API function:: Get individual items by id
@app.route("/item/<id>", methods=["GET"])
def get_item_by_id(id):
    item = Item.query.get(id)
    return item_schema.jsonify(item)


# API function: Update an item
@app.route("/item/<id>", methods=["PUT"])
def update_item(id):
    item = Item.query.get(id)
    name = request.json["name"]
    description = request.json["description"]
    available = request.json["available"]
    last_ordered = request.json["last_ordered"]

    item.name = name
    item.description = description
    item.available = available
    item.last_ordered = last_ordered

    db.session.commit()

    return item_schema.jsonify(item)


# API function: Delete an item
@app.route("/item/<id>", methods=["DELETE"])
def delete_item(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()

    return item_schema.jsonify(item)


if __name__ == "__main__":
    app.run(debug=True)  # debug set to True for dev env

# todo: add vendors
# todo: add authentication