from fastapi import FastAPI, Path, Query

import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def root():
    return {"message": "patient Management System API"}

@app.get("/health")
def health():
    return {"status": "A fully functional patient management system API"}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str= Path(..., description="Patient ID",example='P0001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {"error": "Patient not found"}
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get('/sort')
def sort_patients(sort_by: str = Query(...,description="Sort on the basis of hright, weight, or bmi,"),order: str= Query('asc',description="Sort in asc or desc order")):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid fields select form : {valid_fields}")

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Order must be 'asc' or 'desc'")
    
    data = load_data()
    
    sort_order = True if order=='desc' else False
    # Sort the data
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    
    return sorted_data