import os

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "LangChain"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    PROJECT_VERSION: str = "1.0.0"

    class Config:
        case_sensitive = True


settings = Settings()
