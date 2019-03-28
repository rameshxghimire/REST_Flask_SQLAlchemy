#REST API with Flask
A CRUD RESTful API using Flask and SQLAlchemy. 
The default SQLite database is used for the database. 


The API allows the following functionality:

_1. Add an item_

`address     : url/item`

`method      : POST`

`content type: application/json`

_2. Update an item (by id)_

`address     : url/item/<id>`

`method      : PUT`

`content type: application/json`

_3. Get all item_

`address     : url/items`

`method      : GET`

`content type: application/json`

_4. Delete an item_

`address     : url/item/id`

`method      : DELETE`

`content type: application/json`

_5. Get an item by id_

`address     : url/item/<id>`

`method      : GET`

`content type: application/json`