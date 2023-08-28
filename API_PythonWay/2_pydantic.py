from fastapi import FastAPI, HTTPException
# from starlette import status
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI() # create an app from fastapi 

# create a book class
class Book:
    id: int 
    title: str
    author: str
    description: str
    rating: int 

    def __init__(self,id,title,author,description,rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating =rating


# Pydantic class -  data validation 
class BookRequest(BaseModel): 
    id: Optional[int] = None 
    title: str = Field(min_length=3,)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

    class Config: # for more descriptive documentation in Swagger UI
        pass 

books = [Book(1, "Title 1", "Author 1", "Description 1", 5),
         Book(2, "Title 2", "Author 2", "Description 2", 5),
         Book(3, "Title 3", "Author 3", "Description 3", 2),
         Book(4, "Title 4", "Author 4", "Description 4", 1)]

# GET
@app.get("/books")
def read_all_books():
    return books

# POST
@app.post("/create_book")
def create_book(book_request : BookRequest):
    print(type(book_request))
    new_book = Book(**book_request.model_dump())
    books.append(add_incremental(new_book))
    return books


def add_incremental(book):
    if len(books) == 0:
        book.id = 1
    else:
        book.id = len(books) + 1   
    return book


