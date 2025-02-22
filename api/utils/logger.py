import logging
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime
from fastapi import Request

# Configurar logging global
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = datetime.utcnow()
        response = await call_next(request)
        process_time = (datetime.utcnow() - start_time).total_seconds()
        
        logging.info(f"{request.method} {request.url} - {response.status_code} - {process_time:.3f}s")
        
        return response
