# my-brain
My own AI agent

My intent is to create a agent that runs locally without cost. The first focus of it is to write code. Good code.
It will run the AI model with Ollama.

# How to run this project:

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    uvicorn main:app --reload --host 0.0.0.0 --port 8008

# Request JSON
    
    /message
    {
        'message': str,
        'directory': str
    }

# Response JSON

    /message
    {
        'message': str
    }

# Diary

### August 13
It started working, now the agent can create files with the things that I want. Also, thanks for the Ollama documentation, they have a nice entry to agentic loop there. Also, the fibonacci.py file in this project is the first file created by the agent, so, it's like a milestone and will be in this project forever.

### August 14
Reorganized the whole project, each thing in the right place, creating the base to expand in future. Also, I included a final answer from the model telling if the task is compleated or not. The way this agent is going to work is that you and him will build the project togheter, so, he will not know all the things, how to create everything, the ideia is the user and the agent learn throw the whole process of a project. So, if you want the agent to create a new feature, first he needs to know how to do it right.
Also, I have moved the files that the agent creates at my tests to the agent_creations folder.

### August 15
Started in the UI. First, I had to modify my python project to be an API using FastAPI. I'm using SwiftUI as my UI framework for it, get a nice macOS looking for it.

### August 17
Today I'm ending my first version. It has only a ugly front-end with two text boxes and one button to send a request to this API, I'm making it with SwiftUI, Claude helped me a lot, I didn't understand much about how to use SwiftUI correctly, so, I'm improvising for now, to have only a structure capable of testing it. I messed up the returning of the API, I was only sending a text that was not in a JSON format, so I'm fixing that right now.

### August 18
Asked Claude to improve the Front-End, I was not happy with SwiftUI. I have changed the API to accept a directory parameter, to define where the agent will create the file.