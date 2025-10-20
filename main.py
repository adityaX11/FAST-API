## command for start the server of python(uvicorn)-> uvicorn main:app --reload

from fastapi import FastAPI

app=FastAPI()  ## use FAST-api as object.

@app.get("/") ## create a route.
def hello():
    return {'message':'Hello I Aditya'}

@app.get("/about")
def intro():
    return {'About':'Hii I am an Engineer.Currently Study in 3rd year'}
