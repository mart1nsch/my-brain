from tools.tools import create_file


available_functions = {
    'names': ['create_file'],
    'functions': [create_file]
}


def _get_tool(function_name:str):
    function_index = available_functions['names'].index(function_name)
    return available_functions['functions'][function_index]


def _execute_tool(tool_calls) -> str:
    return str(_get_tool(tool_calls.function.name)(**tool_calls.function.arguments))


def manage_tool_calls(tool_calls:list) -> list[dict]:
    tool_results = []

    for tc in tool_calls:
        if tc.function.name in available_functions['names']:
            result = _execute_tool(tc)
            tool_results.append({
                'role': 'tool',
                'tool_name': tc.function.name,
                'content': result
            })
    return tool_results