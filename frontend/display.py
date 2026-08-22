from rich.markdown import Markdown
from frontend.config import ACCENT_COLOR, SYSTEM_COLOR, ERROR_COLOR


def banner_text(directory:str) -> str:
    return '[' + ACCENT_COLOR + ']my-brain agent[/' + ACCENT_COLOR + ']  working directory: ' + directory


def assistant_body(text:str) -> Markdown:
    return Markdown('• ' + text)


def error_line(text:str) -> str:
    return '[' + ERROR_COLOR + ']' + text + '[/' + ERROR_COLOR + ']'


def system_line(text:str) -> str:
    return '[' + SYSTEM_COLOR + ']' + text + '[/' + SYSTEM_COLOR + ']'


def help_text() -> str:
    return (
        '[' + SYSTEM_COLOR + ']'
        '/dir          show the current working directory\n'
        '/dir <path>   set the working directory\n'
        '/help         show this message\n'
        '/exit, /quit  leave the chat'
        '[/' + SYSTEM_COLOR + ']'
    )
