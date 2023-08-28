from pydantic import BaseModel


class Employee(BaseModel):
    id: int
    name: str
    personal_id: int
    biometric: list
    pic: list


class EmployeeRequest(BaseModel):
    name: str
    personal_id: int
    biometric: list
    pic: list


class EmployeeResponse(BaseModel):
    id: int
    name: str
    personal_id: int
    biometric: list
    pic: list
    created_at: str
