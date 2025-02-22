from pydantic import BaseModel

class DepartmentBase(BaseModel):
    department: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    id: int

    class Config:
        from_attributes = True


        