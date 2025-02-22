from pydantic import BaseModel
from typing import List, Dict, Any

class BatchInsertResponse(BaseModel):
    inserted: List[Dict[str, Any]]  
    rejected: List[Dict[str, Any]]  