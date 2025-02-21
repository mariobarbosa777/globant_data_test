from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    General Application settings class.
    """

    class Config:
        """
        Get env variables from dotenv file.
        """
        env_file = ".env"

    # ---- APP ---- #
    ENV: str
    DATABASE_URL:str 


settings = Settings()