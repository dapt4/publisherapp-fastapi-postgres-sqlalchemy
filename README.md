# publisherapp-fastapi-postgres-sqlalchemy

first create your virtualenv

`$ python3 -m venv venv`

activate venv

`$ source venv/bin/activate`

then install requirements

`$ pip install -r requirements.txt`

install postgresql, login and create the database

`CREATE DATABASE <yourDBname>;`

create a .env file in the root folder

`$ touch .env`

and add your postgresql url to .env file

>ENV_URL='postgresql+psycopg2://{yourDbUsername}:{yourDbPass}@{yourHost or localhost}/{yourDBname}'

finally the project run with: 

`$ uvicorn main:app`

open your browser or your http Client in: 

### get all publisher 
`GET http://localhost:8000/publisher`
### get a publisher 
`GET http://localhost:8000/publisher/<publisher_code>`
### create a new publisher 
`POST http://localhost:8000/publisher`
### edit a publisher 
`PUT http://localhost:8000/publisher/<publisher_code>`
### delete a publisher 
`DELETE http://localhost:8000/task/<publisher_code>`

### get all book 
`GET http://localhost:8000/book`
### get a book 
`GET http://localhost:8000/book/<isbn>`
### create a new book 
`POST http://localhost:8000/book/<publisher_code>`
### edit a book 
`PUT http://localhost:8000/book/<isbn>/<publisher_code>`
### delete a book 
`DELETE http://localhost:8000/book/<isbn>`

### get all edition 
`GET http://localhost:8000/edition`
### get a edition 
`GET http://localhost:8000/edition/<isbn>`
### create a new edition 
`POST http://localhost:8000/edition/<isbn>/<publisher_code>`
