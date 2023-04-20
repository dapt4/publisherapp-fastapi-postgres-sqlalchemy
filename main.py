from fastapi import FastAPI
from database.create_tables import create_tables
from database.db import engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.models import Publisher, Book, Edition
from models.pydantic_models import pyPublisher, pyBook, pyEdition

app = FastAPI()

# create_tables() # uncomment this line to create tables

@app.get("/publisher")
async def get_publishers():
    try:
        with Session(engine) as session:
            stmt = select(Publisher)
            publishers = session.scalars(stmt)
            result = [publisher.to_dict() for publisher in publishers]
            return result
    except Exeption as err:
        print(err)

@app.get("/publisher/{code}")
def get_publisher(code: str):
    try:
        with Session(engine) as session:
            stmt = select(Publisher).where(Publisher.code == code)
            publisher = session.scalars(stmt).one()
            return publisher.to_dict()
    except Exception as err:
        print(err)

@app.post("/publisher")
def new_publisher(publisher: pyPublisher):
    try:
        with Session(engine) as session:
            pub = Publisher(code=publisher.code, name=publisher.name)
            session.add(pub)
            session.commit()
            return pub.to_dict()
    except Exeption as err:
        print(err)

@app.put("/publisher/{code}")
def update_publisher(publisher: pyPublisher, code: str):
    try:
        with Session(engine) as session:
            stmt = select (Publisher).where(Publisher.code == code)
            pub = session.scalars(stmt).one()
            pub.code = publisher.code
            pub.name = publisher.name
            session.commit()
    except Exception as err:
        print(err)

@app.delete("/publisher/{code}")
def delete_publisher(code: str):
    try:
        with Session(engine) as session:
            publisher = session.get(Publisher, code)
            session.delete(publisher)
            session.commit()
            return publisher.to_dict()
    except Exception as err:
        print(err)

@app.get("/book")
def get_books():
    try:
        with Session(engine) as session:
            stmt = select(Book)
            books = session.scalars(stmt)
            return [book.to_dict() for book in books]
    except Exception as err:
        print(err)

@app.get("/book/{isbn}")
def get_book(isbn: str):
    try:
        with Session(engine) as session:
            stmt = select(Book).where(Book.isbn==isbn)
            book = session.scalars(stmt).one()
            return book.to_dict()
    except Exception as err:
        print(err)

@app.post("/book/{publisher}")
def new_book(book: pyBook, publisher: str):
    try:
        with Session(engine) as session:
            new_book = Book(title=book.title, isbn=book.isbn)
            result = session.add(new_book)
            new_edition = Edition(
                    isbn=new_book.isbn,
                    publisher_code=publisher
                    )
            session.add(new_edition)
            session.commit()
            return new_book.to_dict()
    except Exception as err:
        print(err)

@app.put('/book/{isbn}/{publisher_code}')
def update_book(isbn:str, publisher_code:str, book: pyBook):
    try:
        with Session(engine) as session:
            stmt = select(Book).where(Book.isbn == isbn)
            bk = session.scalars(stmt).one()
            bk.isbn = book.isbn
            bk.title = book.title
            edition = Edition(isbn=bk.isbn, publisher_code=publisher_code)
            session.add(edition)
            session.commit()
            return bk.to_dict()
    except Exception as err:
        print(err)

@app.delete("/book/{isbn}")
def delete_book(isbn: str):
    try:
        with Session(engine) as session:
            book = session.get(Book, isbn)
            session.delete(book)
            session.commit()
            return book.to_dict()
    except Exception as err:
        print(err)

@app.get("/edition")
def get_editions():
    try:
        with Session(engine) as session:
            stmt = select(Edition)
            editions = session.scalars(stmt)
            return [edition.to_dict() for edition in editions]
    except Exception as err:
        print(err)

# function for get a edition
@app.get("/edition/{isbn}")
def get_edition(isbn: str):
    try:
        with Session(engine) as session:
            stmt = select(Edition).where(Edition.isbn == isbn)
            edition = session.scalars(stmt).one()
            return edition.to_dict()
    except Exception as err:
        print(err)

# function for create a edition
@app.post("/edition/{isbn}/{publisher_code}")
def new_edition(isbn: str, publisher_code: str):
    try:
        with Session(engine) as session:
            edition = Edition(isbn=isbn, publisher_code=publisher_code)
            session.add(edition)
            session.commit()
            return edition.to_dict()
    except Exception as err:
        print(err)

