from pydantic import BaseModel
from pathlib import Path


class Settings:
    directory: str = str(Path().absolute())


class RequestAgent(BaseModel):
    message: str


class ResponseAgent(BaseModel):
    message: str


class RequestDirectory(BaseModel):
    directory: str


settings = Settings()