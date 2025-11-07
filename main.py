## command for start the server of python(uvicorn)-> uvicorn main:app --reload

from fastapi import FastAPI,Path,HTTPException,Query
## HTTPException-> its is an special built-in exception ithingn Fast-api used for return custom HTTP error response when something is gone wrong.
# why path function use in Fast API, it is use to give some hints like (rules , validation,metadata, and documentation) for routers. that help the devs as well as users to use it.
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

@app.get('/patient/{patient_id}') ## this route use for particular patient data.
def view_patient(patient_id:str=Path(...,description='ID of patient in Database.',example="P001")): ## what is meaning of ... here in path its denote the something is imp/required that declare for the path.
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    # return {"Error":"Patient not found."} its always http status is ok 200
    raise HTTPException(status_code=404,detail="Patient not found")

@app.get('/sort')
def sort_data(sort_by:str=Query(...,description='Sort on the bases of height,weight and BMI'),order:str=Query('asc',description='sort in asc or desc order.')):## query parameter basically send the additional or extra info to the backend (? after the all thing is the query parameter in the router.)start from ?,each parameters are key-vale and seperated by &.
    valid_rang=['height','weight','bmi']
    if sort_by not in valid_rang:
        raise HTTPException(status_code=400,detail='Invalid field selected from{valid_rang}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order select b/w asc and desc.')

    data = load_data()
    sort_order=True if order=='desc'else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order) ##because Python uses reverse=True for descending order).
    return sorted_data