from database.db import engine
from sqlalchemy import MetaData
from models.models import Book, Publisher, Edition


def create_tables():
    metadata = MetaData()
    metadata.create_all(engine, tables=[
        Book.__table__,
        Publisher.__table__,
        Edition.__table__])

