from fastapi import HTTPException, FastAPI, Path, Query
from starlette import status
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
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    # rating: int = Field(gt=0, lt=6)

    class Config: # inner class 
        json_schema_extra = {"example" : {"title" : "a new title" ,
                                          "author" : "a new author",
                                          "description":"a new description",
                                           "rating" : 3}}

    
books = [Book(1, "Title 1", "Author 1", "Description 1", 5),
         Book(2, "Title 2", "Author 2", "Description 2", 5),
         Book(3, "Title 3", "Author 3", "Description 3", 2),
         Book(4, "Title 4", "Author 4", "Description 4", 1)]



# GET  - Find all books
@app.get("/books", status_code=status.HTTP_404_NOT_FOUND)
def read_all_books():
    print("Hello")
    return {"books" : books}



# query parameter
@app.put("/books/update_book")
def update_book(updated_book: BookRequest):
    for book in books: 
        if book.id == updated_book.id:
            books.remove(book)
            books.append(updated_book)
            break



