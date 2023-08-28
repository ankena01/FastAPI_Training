#  Query Parameter
from fastapi import FastAPI
app = FastAPI() # create an app from fastapi 


books = [{'title': 'Title One' , 'author' : 'Author One', 'category' : 'science'},
         {'title': 'Title Two' , 'author' : 'Author Two', 'category' : 'science'},
         {'title': 'Title Three' , 'author' : 'Author Three', 'category' : 'history'},
         {'title': 'Title Four' , 'author' : 'Author Four', 'category' : 'math'}]

# find books based on category using query parameter
# Query
@app.get("/books/")
def get_books_category_query(category: str):
    books_to_return = []
    for book in books:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Path

# @app.get("/books/{book_author}")
# def get_book(book_author: str, ):
#     books_to_return = []
#     for book in books:
#         if book.get("author").casefold() == book_author.casefold():
#             books_to_return.append(book)
#     return books_to_return

@app.get("/books/{book_category}")
def get_book(book_category: str, ):
    books_to_return = []
    for book in books:
        if book.get("category").casefold() == book_category.casefold():
            books_to_return.append(book)
    return books_to_return




