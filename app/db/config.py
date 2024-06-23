import os
from pydantic_settings import BaseSettings
from typing import ClassVar
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):

    DATABASE_URL: ClassVar[str] = os.getenv("DATABASE_URL")

    @property
    def DATABASE_URL_psycopg(self) -> str:
        return self.DATABASE_URL

settings = Settings()
