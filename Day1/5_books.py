# POST METHOD

from fastapi import FastAPI, Body


app = FastAPI() # create an app from fastapi 


books = [{'title': 'Title One' , 'author' : 'Author One', 'category' : 'science'},
         {'title': 'Title Two' , 'author' : 'Author Two', 'category' : 'science'},
         {'title': 'Title Three' , 'author' : 'Author Three', 'category' : 'history'},
         {'title': 'Title Four' , 'author' : 'Author Four', 'category' : 'math'}]

# post
@app.post('/books/create_book')
def create_book(new_book = Body()):
    books.append(new_book)

# get

@app.get("/books")
def fetch_books():
    return books

# get reqests with body are not allowed
# @app.get("/books")
# def fetch_books(new_book=Body()):
#     return new_book
