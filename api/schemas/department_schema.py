from pydantic import BaseModel, Field
from typing import List

class DepartmentBase(BaseModel):
    department: str = Field(..., min_length=1, max_length=255, description="Nombre del departamento")

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    id: int

    class Config:
        from_attributes = True

class DepartmentBatchCreate(BaseModel):
    departments: List[DepartmentCreate] = Field(..., min_length=1, max_length=1000)
