from pydantic import BaseModel

class pyBook(BaseModel):
    isbn: str
    title: str

class pyPublisher(BaseModel):
    code: str
    name: str

class pyEdition(BaseModel):
    id: int
    isbn: str
    publisher_code: str
    date: str

