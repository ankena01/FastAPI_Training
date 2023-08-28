# Path Parameters

# 1. Dynamic Path Parameter

from fastapi import FastAPI
app = FastAPI() # create an app from fastapi 


books = [{'title': 'Title One' , 'author' : 'Author One', 'category' : 'science'},
         {'title': 'Title Two' , 'author' : 'Author Two', 'category' : 'science'},
         {'title': 'Title Three' , 'author' : 'Author Three', 'category' : 'history'},
         {'title': 'Title Four' , 'author' : 'Author Four', 'category' : 'math'}]


# @app.get("/books/{dynamic_param}")
# def read_all_books(dynamic_param):
#     return {"dynamic_param" : dynamic_param}

# @app.get("/books/1/book_one")
# def read_all_books():
#     return {"Book Title" : "My favourate book"}


# run selective data based on path parameter

# Request url -> http://127.0.0.1:8000/books/title%20four


@app.get("/books/{dynamic_param}")
def read_book(dynamic_param: str):
    for book in books:
        if book.get("title").casefold() == dynamic_param.casefold():
            return book
        


