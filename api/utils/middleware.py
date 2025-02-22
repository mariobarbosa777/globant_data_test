from fastapi.middleware.cors import CORSMiddleware

def setup_middlewares(app):
    """Configura los middlewares de la aplicación"""
    
    # Middleware de CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Permitir todas las conexiones (ajustar en producción)
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
