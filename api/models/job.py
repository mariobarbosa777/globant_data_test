from sqlalchemy import Column, Integer, String
from .base import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    job = Column(String, unique=True, nullable=False)
