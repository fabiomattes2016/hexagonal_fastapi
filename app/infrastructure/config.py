import os

from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    URL: str = os.getenv("SQLALCHEMY_DATABASE_URL")
    DATABASE_URL: str = f"{URL}"

    # JWT
    JWT_SECRET: str = os.getenv('JWT_SECRET')
    JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM')
    JWT_TOKEN_EXPIRE_MIN: int = int(os.getenv('JWT_TOKEN_EXPIRE_MIN'))


def get_settings() -> Settings:
    return Settings()
