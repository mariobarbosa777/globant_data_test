from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import Department, Job, HiredEmployee
from schemas.department_schema import DepartmentCreate
from schemas.job_schema import JobCreate
from schemas.employee_schema import EmployeeCreate
from utils.error_handler import handle_rejected_record
from sqlalchemy.exc import IntegrityError
from fastapi import Request

LIMIT = 1000  # 🔹 Límite máximo de registros a devolver

async def insert_record(db: AsyncSession, model, data):
    """
    Inserta un único registro en la base de datos.
    """
    try:
        record = model(**data)
        db.add(record)
        await db.commit()
        await db.refresh(record)
        return record
    except IntegrityError:
        await db.rollback()
        return None  

async def process_batch_insert(db: AsyncSession, request: Request, model, table_name: str, batch_data: list[dict]):
    """
    Procesa la inserción de un batch de registros.  
    - Inserta registros válidos en la tabla correspondiente.  
    - Registra los fallidos en `rejected_records`.  
    """
    inserted_records = []
    rejected_records = []

    for data in batch_data:
        record = await insert_record(db, model, data)
        if record:
            inserted_records.append(record)
        else:
            rejected_records.append(data)

    if rejected_records:
        await handle_rejected_record(request, db, table_name, rejected_records, "IntegrityError: Registro duplicado o inválido")

    return inserted_records 
        

# 📌 Funciones para Departments
async def get_all_departments(db: AsyncSession):
    result = await db.execute(select(Department).limit(LIMIT))  # 🔥 Aplica el límite
    return result.scalars().all()

async def create_departments_batch(
    db: AsyncSession, 
    department_batch: list[DepartmentCreate],
    request: Request
    ):
    
    return await process_batch_insert(db, request, Department, "departments", [dep.dict() for dep in department_batch])



# 📌 Funciones para Jobs
async def get_all_jobs(db: AsyncSession):
    result = await db.execute(select(Job).limit(LIMIT))  # 🔥 Aplica el límite
    return result.scalars().all()

async def create_jobs_batch(
    db: AsyncSession, 
    job_batch: list[JobCreate],
    request: Request
    ):

    return await process_batch_insert(db, request, Job, "jobs", [job.dict() for job in job_batch])

# 📌 Funciones para Employees
async def get_all_employees(db: AsyncSession):
    result = await db.execute(select(HiredEmployee).limit(LIMIT))  # 🔥 Aplica el límite
    return result.scalars().all()

async def create_employees_batch(
    db: AsyncSession, 
    employee_batch: list[EmployeeCreate],
    request: Request
    ):

    return await process_batch_insert(db, request, HiredEmployee, "hired_employees", [emp.dict() for emp in employee_batch])
