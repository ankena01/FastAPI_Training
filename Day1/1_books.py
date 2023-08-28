# Imports

from fastapi import FastAPI

app = FastAPI() # create an app from fastapi 

@app.get("/api-endpoint")
def first_api():
    return {"message":"Lets get started with fast API"}




