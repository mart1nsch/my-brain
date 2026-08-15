from ollama import chat
from agent.config import MODEL, SYSTEM_PROMPT
from tools.manage_tools import available_functions, manage_tool_calls


def _show_final_message(messages:list[dict]) -> None:
    print(messages[-1]['content'])


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
    messages = [
        {
            'role': 'system',
            'content': SYSTEM_PROMPT
        },
        {
            'role': 'user',
            'content': interaction
        }
    ]
    messages = _agentic_loop(messages)
    _show_final_message(messages)