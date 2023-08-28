from fastapi import FastAPI, Body, HTTPException
from starlette import status

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
def create_book(book_request = Body()):
    books.append(book_request)
    # raise HTTPException(status_code=status.HTTP_201_CREATED, detail="Success")
    return books





# PUT
# DELETE
