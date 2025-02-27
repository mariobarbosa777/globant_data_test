from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas.common import BatchInsertResponse
from schemas.department_schema import DepartmentBatchCreate, DepartmentResponse
from schemas.job_schema import JobBatchCreate, JobResponse
from schemas.employee_schema import EmployeeBatchCreate, EmployeeResponse
from services.crud_service import (
    get_all_departments, create_departments_batch,
    get_all_jobs, create_jobs_batch,
    get_all_employees, create_employees_batch
)

router = APIRouter()

# 📌 Endpoints CRUD para Departments
@router.get("/departments/", response_model=list[DepartmentResponse])
async def list_departments(db: AsyncSession = Depends(get_db)):
    return await get_all_departments(db)

@router.post("/departments/batch/", response_model=BatchInsertResponse)
async def add_departments_batch(
    request: Request,
    department_batch: DepartmentBatchCreate, 
    db: AsyncSession = Depends(get_db)
):
    return await create_departments_batch(db, department_batch.departments, request)


# 📌 Endpoints CRUD para Jobs
@router.get("/jobs/", response_model=list[JobResponse])
async def list_jobs(db: AsyncSession = Depends(get_db)):
    return await get_all_jobs(db)

@router.post("/jobs/batch/", response_model=BatchInsertResponse)
async def add_jobs_batch(
    request: Request,
    job_batch: JobBatchCreate, 
    db: AsyncSession = Depends(get_db)
):
    return await create_jobs_batch(db, job_batch.jobs, request)


# 📌 Endpoints CRUD para Employees
@router.get("/employees/", response_model=list[EmployeeResponse])
async def list_employees(db: AsyncSession = Depends(get_db)):
    return await get_all_employees(db)
    
@router.post("/employees/batch/", response_model=BatchInsertResponse)
async def add_employees_batch(
    request: Request,
    employee_batch: EmployeeBatchCreate, 
    db: AsyncSession = Depends(get_db)
):
    return await create_employees_batch(db, employee_batch.employees, request)
