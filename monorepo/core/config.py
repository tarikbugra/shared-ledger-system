from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv


@dataclass
class Config:
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    LEDGER_OPERATION_CONFIG = {
        "DAILY_REWARD": 1,
        "SIGNUP_CREDIT": 3,
        "CREDIT_SPEND": -1,
        "CREDIT_ADD": 10,
        "CONTENT_CREATION": -5,
        "CONTENT_ACCESS": 0,
    }

    def get_database_URI(self):
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


load_dotenv()

settings = Config(
    POSTGRES_DB=getenv("POSTGRES_DB"),
    POSTGRES_USER=getenv("POSTGRES_USER"),
    POSTGRES_PASSWORD=getenv("POSTGRES_PASSWORD"),
    POSTGRES_HOST=getenv("POSTGRES_HOST"),
    POSTGRES_PORT=getenv("POSTGRES_PORT"),
)
