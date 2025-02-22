from fastapi import FastAPI
from config import settings
# from api.routers import departments, jobs, employees
from utils.logger import LoggingMiddleware
from utils.middleware import setup_middlewares  

# Inicializar FastAPI
app = FastAPI(
    title="Globant Data API",
    description="API para manejar datos de empleados, departamentos y trabajos",
    version="1.0"
)



# Configurar middlewares
setup_middlewares(app)
app.add_middleware(LoggingMiddleware)

# # Registrar routers
# app.include_router(departments.router, prefix="/departments", tags=["Departments"])
# app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
# app.include_router(employees.router, prefix="/employees", tags=["Employees"])

# Endpoint de Health Check
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}

# Mensaje en consola al iniciar la API
@app.on_event("startup")
async def startup_event():
    print(f"🚀 API iniciada en modo: {settings.ENV}")
