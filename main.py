from agent.call import execute
from fastapi import FastAPI
from pydantic import BaseModel


class Request(BaseModel):
    message: str


app = FastAPI()


@app.get('/test')
def test() -> None:
    return {
        'status': 'running'
    }


@app.post('/message')
def main(message:Request) -> None:
    return execute(message.message)