from agent.call import execute
from config.settings import settings, RequestAgent, ResponseAgent, RequestDirectory
from fastapi import FastAPI


app = FastAPI()


@app.get('/test')
def test() -> dict:
    return { 'status': 'running' }


@app.get('/directory')
def get_directory() -> ResponseAgent:
    return ResponseAgent(message=settings.directory)


@app.post('/message')
def agent_loop(request:RequestAgent) -> ResponseAgent:
    return ResponseAgent(message=execute(request.message))


@app.post('/directory')
def set_directory(request:RequestDirectory) -> dict:
    try:
        settings.directory = request.directory
        return { 'response': 'success' }
    except Exception as e:
        return { 'response': 'Error: ' + str(e) }