from sqlalchemy import Column, Integer, String
from .base import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    department = Column(String, unique=True, nullable=False)