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
@app.get("/books")
def read_all_books():
    return {"books" : books,
             "message" : HTTPException(status_code=status.HTTP_200_OK,detail="Fetch was succesfull")}



# find book based on rating
@app.get("/books/book_rating")
# def find_book_based_id_query(book_rating : int = Query(gt=-1, lt=6)):
def find_book_based_id_query(book_rating : int):
    books_to_return = []
    for book in books:
        if book.rating == book_rating:
            books_to_return.append(book)
    # return books_to_return
    if len(books_to_return) < 1:
        raise HTTPException(status_code=status.HTTP_200_OK,detail="Fetch was succesfull. However no book found")
    return {"data" : books_to_return,
            "message" : HTTPException(status_code=status.HTTP_200_OK,detail="Fetch was succesfull")}
    
# create an enpoint to update book with specific id

@app.patch("/books/patch")
def book_patch(bookrequest: BookRequest):
    for book in books:
        if book.id == bookrequest.id:
            books.remove(book)
            books.append(bookrequest)
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Patch was succesfull")
       
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book to be patched not found")


#  create an endpoint to delete the book based on id

@app.delete("/books/delete")
def delete_book(book_id : int):
    flag = False 
    for book in books: 
        if book.id == book_id:
            books.remove(book)
            flag = True
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Book removed successfully")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

