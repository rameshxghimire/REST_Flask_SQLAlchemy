# One Pager REST API with Flask
## Splitting up and extending recommended

This is a one file API which can be taken as example for how flasks works. I do not recommend using it for production because it is very barebones and does not take into account best practices and other concerns. Instead of modifying this to make it production ready, I can add a completely new project if I get a request to do so.

If you want to extend it and continue working on it , send a pull request.

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
