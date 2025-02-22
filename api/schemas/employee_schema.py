from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class EmployeeBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255, description="Nombre del empleado")
    datetime: datetime = Field(..., description="Fecha y hora de contratación")
    department_id: int = Field(..., gt=0, description="ID del departamento al que pertenece")
    job_id: int = Field(..., gt=0, description="ID del trabajo asignado")

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        from_attributes = True

class EmployeeBatchCreate(BaseModel):
    employees: List[EmployeeCreate] = Field(..., min_length=1, max_length=1000)
