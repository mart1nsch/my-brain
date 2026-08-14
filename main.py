from ollama import chat, ChatResponse


def create_file(filename:str, content:str) -> int:
    """"Create a file in the project"""
    """"
    Args:
    filename: Filename WITH extension
    content: The content to be written in the file

    Returns:
    0 if created with success, 1 if not
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception:
        return False


available_functions = {
    'create_file': create_file
}


def main() -> None:
    while True:
        messages = [
            {
                'role': 'system',
                'content': "You're Martin Schneider's personal coding agent. Only do what he's asking, nothing more."
            },
            {
                'role': 'user',
                'content': input('ask something: ')
            }
        ]

        while True:
            response: ChatResponse = chat(
                model='gemma4:e2b-it-qat',
                messages=messages,
                tools=[create_file],
                think=True,
            )

            messages.append(response.message)
            print("Thinking: ", response.message.thinking, end='\n\n\n')
            print("Content: ", response.message.content, end='\n\n\n')

            if response.message.tool_calls:
                for tc in response.message.tool_calls:
                    if tc.function.name in available_functions:
                        print(f"Calling {tc.function.name} with arguments {tc.function.arguments}")
                        result = available_functions[tc.function.name](**tc.function.arguments)
                        print(f"Result: {result}")
                        # add the tool result to the messages
                        messages.append({'role': 'tool', 'tool_name': tc.function.name, 'content': str(result)})
            else:
                # end the loop when there are no more tool calls
                break
        # continue the loop with the updated messages


if __name__ == '__main__':
    main()