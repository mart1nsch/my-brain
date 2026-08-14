from ollama import chat, ChatResponse


MODEL = 'gemma4:e2b-it-qat'


def call(content:str, no_ollama:bool = False) -> str:
    if not no_ollama:
        response: ChatResponse = chat(
            model=MODEL,
            messages=[
                {
                    'role': 'user',
                    'content': content,
                },
            ],
            options={
                'temperature': 0.1
            })
        return response['message']['content']
    return "That's all folks"