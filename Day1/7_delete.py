from fastapi import FastAPI, Body
app = FastAPI() # create an app from fastapi 


books = [{'title': 'Title One' , 'author' : 'Author One', 'category' : 'science'},
         {'title': 'Title Two' , 'author' : 'Author Two', 'category' : 'science'},
         {'title': 'Title Three' , 'author' : 'Author Three', 'category' : 'history'},
         {'title': 'Title Four' , 'author' : 'Author Four', 'category' : 'math'}]

@app.delete("/books/delete_book/{book_title}")
def delete_book(book_title: str):
    counter = 0
    for book in books:
        if book.get('title').casefold() == book_title.casefold():
            books.pop(counter)
            break
        counter = counter + 1

# get
@app.get("/books")
def fetch_books():
    return books