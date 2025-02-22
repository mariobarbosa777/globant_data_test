from sqlalchemy import Column, Integer, String
from .base import BaseModel

class Department(BaseModel):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    department = Column(String, unique=True, nullable=False)