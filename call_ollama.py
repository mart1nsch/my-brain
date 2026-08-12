from ollama import chat, ChatResponse


MODEL = 'gemma4:e2b-it-qat'


def call(content:str) -> str:
    response: ChatResponse = chat(model=MODEL, messages=[
        {
            'role': 'user',
            'content': content,
        },
    ])
    return response['message']['content']