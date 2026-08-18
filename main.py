from agent.call import execute
from fastapi import FastAPI
from pydantic import BaseModel


class Request(BaseModel):
    message: str


class Response(BaseModel):
    message: str


app = FastAPI()


@app.get('/test')
def test() -> None:
    return {
        'status': 'running'
    }


@app.post('/message')
def main(message:Request) -> Response:
    return Response(message=execute(message.message))