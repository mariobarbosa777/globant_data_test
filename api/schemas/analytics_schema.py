from pydantic import BaseModel

class QuarterlyHiringReport(BaseModel):
    department: str
    job: str
    Q1: int
    Q2: int
    Q3: int
    Q4: int

class HighHiringDepartments(BaseModel):
    id: int
    department: str
    total_hired: int