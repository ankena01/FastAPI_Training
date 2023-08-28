from fastapi import FastAPI, Body
app = FastAPI() # create an app from fastapi 


books = [{'title': 'Title One' , 'author' : 'Author One', 'category' : 'science'},
         {'title': 'Title Two' , 'author' : 'Author Two', 'category' : 'science'},
         {'title': 'Title Three' , 'author' : 'Author Three', 'category' : 'history'},
         {'title': 'Title Four' , 'author' : 'Author Four', 'category' : 'math'}]

# @app.put("/books/update_book")
# def update_book(update_book=Body()):
    
#     for book in books:
#         counter = 0
#         if book.get("title").casefold() == update_book.get("title").casefold():
#             books[counter] = update_book
#             return books
#         counter = counter + 1

@app.patch("/books/patch_book")
def update_book(update_book=Body()):
    
    for book in books:
        counter = 0
        if book.get("title").casefold() == update_book.get("title").casefold():
            books[counter] = update_book
            return books
        counter = counter + 1