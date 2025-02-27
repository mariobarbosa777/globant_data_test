from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from api.database import get_db
from api.schemas.analytics_schema import QuarterlyHiringReport

router = APIRouter()

@router.get("/quarterly-hiring", response_model=List[QuarterlyHiringReport])
async def quarterly_hiring_report(db: AsyncSession = Depends(get_db)):
    query = text("""
        SELECT 
            d.department,
            j.job,
            SUM(CASE WHEN EXTRACT(QUARTER FROM he.datetime) = 1 THEN 1 ELSE 0 END) AS "Q1",
            SUM(CASE WHEN EXTRACT(QUARTER FROM he.datetime) = 2 THEN 1 ELSE 0 END) AS "Q2",
            SUM(CASE WHEN EXTRACT(QUARTER FROM he.datetime) = 3 THEN 1 ELSE 0 END) AS "Q3",
            SUM(CASE WHEN EXTRACT(QUARTER FROM he.datetime) = 4 THEN 1 ELSE 0 END) AS "Q4"
        FROM hired_employees he
        JOIN departments d ON he.department_id = d.id
        JOIN jobs j ON he.job_id = j.id
        WHERE 
            EXTRACT(YEAR FROM he.datetime) = 2021 
        GROUP BY d.department, j.job
        ORDER BY d.department, j.job
    """)
    result = await db.execute(query)
    rows = result.mappings().all()  # Devuelve una lista de diccionarios
    return rows
