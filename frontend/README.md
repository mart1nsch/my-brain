# my-brain frontend

Terminal chat client for the my-brain agent backend.

## Setup

    cd frontend
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Run

Make sure the backend is running first (from repo root):

    uvicorn main:app --reload --host 0.0.0.0 --port 8008

Then, from the repo root (not inside frontend/), with the frontend venv active:

    python3 -m frontend.main

## Commands

    /dir <path>   change the working directory (calls POST /directory)
    /help         list commands
    /exit, /quit  leave

Anything else typed is sent as a chat message to the agent.

## Backend contract this frontend relies on

    POST /message
    { "message": str, "directory": str } -> { "message": str }

    POST /directory
    { "directory": str } -> { "response": str }

    GET /test
    -> { "status": "running" }

Every /message call includes the directory currently known to the frontend,
since the backend's RequestAgent requires it on every request regardless of
prior /directory calls.
