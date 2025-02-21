from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from config import settings
from services.aws_service import get_aws_secret 

def get_database_url():
    if settings.ENV == "local":
        return settings.DATABASE_URL  # Desde .env
    elif settings.ENV == "prd":
        return get_aws_secret('my_secret_name')  # TODO Crear Secreto prd
    else:
        raise ValueError("Invalid ENV")

DATABASE_URL = get_database_url()

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session #Evita agotar las sessiones porque las cierra al acabar
