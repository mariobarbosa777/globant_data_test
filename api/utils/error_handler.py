from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

async def db_exception_handler(request: Request, exc: Exception):
    error_details = {
        "error": str(exc.__class__.__name__),  # 🔹 Tipo de error (ej. IntegrityError)
        "message": str(exc),  # 🔹 Mensaje original del error
        "path": request.url.path  # 🔹 Endpoint donde ocurrió el error
    }

    if isinstance(exc, IntegrityError):
        return JSONResponse(
            status_code=400,
            content={
                "detail": "Integrity constraint violated.",
                "error_details": error_details
            }
        )
    elif isinstance(exc, SQLAlchemyError):
        return JSONResponse(
            status_code=500,
            content={
                "detail": "A database error occurred.",
                "error_details": error_details
            }
        )
    
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Error inesperado.",
            "message": "Ocurrió un error desconocido.",
            "path": request.url.path
        }
    )


async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Error interno del servidor.",
            "message": "Ocurrió un error inesperado. Contacta al soporte si el problema persiste.",
            "path": request.url.path
        }
    )