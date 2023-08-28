import datetime
from typing import List
from data.database import init_db
from fastapi import FastAPI
from data.schemes import employees_table
from data.models import EmployeeRequest, Employee, EmployeeResponse

database = init_db()

app = FastAPI()

def generate_datetime():
    return datetime.datetime.now()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def get_hello():
    return {"Hello": "World"}


@app.get("/employees", response_model=List[EmployeeResponse])
async def read_employees_table():
    try:
        query = employees_table.select()
        employeesDb = await database.fetch_all(query)
        employeesSerialized = []
        for employee in employeesDb:
            employeesSerialized.append({
                "id": employee.id,
                "name": employee.name,
                "personal_id": employee.personal_id,
                "biometric": employee.biometric,
                "pic": employee.pic,
                "created_at": employee.created_at.isoformat()
            })
        return employeesSerialized
        
    except Exception as e:
        print(e)
        return e


@app.post("/employees/", response_model=EmployeeResponse)
async def create_employee(employee: EmployeeRequest):
    created_at = generate_datetime()
    query = employees_table.insert().values(
        name=employee.name,
        personal_id=employee.personal_id,
        biometric=employee.biometric,
        pic=employee.pic,
        created_at=created_at
    )
    last_record_id = await database.execute(query)
    return {
        "id": last_record_id,
        **employee.model_dump(),
        "created_at": created_at.isoformat()
    }
