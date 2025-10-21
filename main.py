## command for start the server of python(uvicorn)-> uvicorn main:app --reload

from fastapi import FastAPI
import json

app=FastAPI()  ## use FAST-api as object.

## fetch the json data(patient records)
def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data

@app.get("/") ## create a route (Home route).
def intro():
    return {'App':'Patients Management System.'}

@app.get("/about") ## about route.
def about():
    return {'About':'A fully Functional API to manage your patient record'}

@app.get("/view") ## this route use for view all record .
def view():
    data = load_data()
    return data