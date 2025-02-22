from pydantic import BaseModel, Field
from typing import List

class JobBase(BaseModel):
    job: str

class JobCreate(JobBase):
    pass

class JobResponse(JobBase):
    id: int

    class Config:
        from_attributes = True

class JobBatchCreate(BaseModel):
    jobs: List[JobCreate] = Field(..., min_length=1, max_length=1000)
