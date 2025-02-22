from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class EmployeeBase(BaseModel):
    name: str
    datetime: datetime
    department_id: int
    job_id: int

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        from_attributes = True

class EmployeeBatchCreate(BaseModel):
    employees: List[EmployeeCreate] = Field(..., min_length=1, max_length=1000)
