from ollama import chat
from agent.config import MODEL, SYSTEM_PROMPT
from tools.manage_tools import available_functions, manage_tool_calls
from db.connection import return_chat_data, include_chat_data


def _assembly_previous_messages() -> list[dict]:
    return [{ 'role': i[1], 'content': i[0] } for i in return_chat_data()]


def _assembly_messages(interaction:str) -> list[dict]:
    messages = _assembly_previous_messages()

    messages.append({
        'role': 'system',
        'content': SYSTEM_PROMPT
    })

    messages.append({
        'role': 'user',
        'content': interaction
    })
    return messages


def _agentic_loop(messages:list[dict]) -> list[dict]:
    while True:
        response = chat(
            model=MODEL,
            messages=messages,
            tools=available_functions['functions'],
            think=True,
        )
        messages.append(response.message)

        if response.message.tool_calls:
            messages.extend(manage_tool_calls(response.message.tool_calls))
        else:
            break
    return messages


def execute(interaction:str) -> None:
    messages = _assembly_messages(interaction)

    messages = _agentic_loop(messages)

    include_chat_data(interaction, 'user')
    include_chat_data(messages[-1]['content'], 'agent')

    return messages[-1]['content']