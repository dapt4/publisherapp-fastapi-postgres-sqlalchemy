import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import (
        DeclarativeBase,
        relationship,
        Mapped,
        mapped_column)

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = 'book'
    isbn: Mapped[str] = mapped_column(String(255), primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    editions: Mapped[list] = relationship('Edition', cascade='all, delete')

    def to_dict(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
        }

class Publisher(Base):
    __tablename__ = 'publisher'
    code: Mapped[str] = mapped_column(String(255), primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    editions: Mapped[list] = relationship('Edition', cascade='all, delete')

    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
        }

class Edition(Base):
    __tablename__ = 'edition'
    id: Mapped[int] = mapped_column(primary_key=True)
    isbn: Mapped[str] = mapped_column(ForeignKey('book.isbn'))
    publisher_code: Mapped[str] = mapped_column(ForeignKey('publisher.code'))
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'isbn': self.isbn,
            'publisher_code': self.publisher_code,
            'date': self.date,
        }
