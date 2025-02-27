from sqlalchemy import Column, Integer, String, TIMESTAMP, Text
from sqlalchemy.dialects.postgresql import JSONB
from .base import BaseModel
from datetime import datetime

class RejectedRecord(BaseModel):
    __tablename__ = "rejected_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    table_name = Column(String(50), nullable=False)
    raw_data = Column(JSONB, nullable=True) 
    error_message = Column(Text, nullable=False)
    rejected_at = Column(TIMESTAMP, default=datetime.utcnow)
