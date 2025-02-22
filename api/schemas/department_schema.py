from pydantic import BaseModel, Field
from typing import List

class DepartmentBase(BaseModel):
    department: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    id: int

    class Config:
        from_attributes = True

class DepartmentBatchCreate(BaseModel):
    departments: List[DepartmentCreate] = Field(..., min_length=1, max_length=1000)
