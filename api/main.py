from fastapi import FastAPI
from config import settings
from routers import crud, analytics
from utils.logger import LoggingMiddleware
from utils.error_handler import db_exception_handler, global_exception_handler
from utils.middleware import setup_middlewares  
from sqlalchemy.exc import SQLAlchemyError

# Inicializar FastAPI
app = FastAPI(
    title="Globant Data API",
    description="API para manejar datos de empleados, departamentos y trabajos",
    version="1.0"
)



# Configurar middlewares
setup_middlewares(app)
app.add_middleware(LoggingMiddleware)

# Agregar manejo global de errores de base de datos
app.add_exception_handler(SQLAlchemyError, db_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)


# # Registrar routers
app.include_router(crud.router, prefix="/crud", tags=["CRUD"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])


# Endpoint de Health Check
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}

# Mensaje en consola al iniciar la API
@app.on_event("startup")
async def startup_event():
    print(f"🚀 API iniciada en modo: {settings.ENV}")
