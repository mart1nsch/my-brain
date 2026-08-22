from pydantic import BaseModel


class Settings:
    directory: str = 'agent_creations'


class RequestAgent(BaseModel):
    message: str


class ResponseAgent(BaseModel):
    message: str


class RequestDirectory(BaseModel):
    directory: str


settings = Settings()