from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import Department, Job, HiredEmployee
from schemas.department_schema import DepartmentCreate
from schemas.job_schema import JobCreate
from schemas.employee_schema import EmployeeCreate

LIMIT = 1000  # 🔹 Límite máximo de registros a devolver

# 📌 Funciones para Departments
async def get_all_departments(db: AsyncSession):
    result = await db.execute(select(Department).limit(LIMIT))  # 🔥 Aplica el límite
    return result.scalars().all()

async def create_departments_batch(db: AsyncSession, department_batch: list[DepartmentCreate]):
    new_departments = [Department(**dep.dict()) for dep in department_batch]
    db.add_all(new_departments)
    await db.commit()
    return new_departments


# 📌 Funciones para Jobs
async def get_all_jobs(db: AsyncSession):
    result = await db.execute(select(Job).limit(LIMIT))  # 🔥 Aplica el límite
    return result.scalars().all()

async def create_jobs_batch(db: AsyncSession, job_batch: list[JobCreate]):
    new_jobs = [Job(**job.dict()) for job in job_batch]
    db.add_all(new_jobs)
    await db.commit()
    return new_jobs

# 📌 Funciones para Employees
async def get_all_employees(db: AsyncSession):
    result = await db.execute(select(HiredEmployee).limit(LIMIT))  # 🔥 Aplica el límite
    return result.scalars().all()

async def create_employees_batch(db: AsyncSession, employee_batch: list[EmployeeCreate]):
    new_employees = [HiredEmployee(**emp.dict()) for emp in employee_batch]
    db.add_all(new_employees)
    await db.commit()
    return new_employees
