from rich.spinner import Spinner
from textual.app import App, ComposeResult
from textual.widgets import RichLog, Input, Static
from textual import work
from frontend.client import send_message, set_directory
from frontend.display import banner_text, assistant_body, error_line, system_line, help_text
from frontend.config import SYSTEM_COLOR


PLACEHOLDER = 'message the agent...'
THINKING_TEXT = 'thinking...'


class AgentApp(App):
    CSS = """
    Screen {
        background: transparent;
    }

    #transcript {
        background: transparent;
        border: none;
        padding: 1 2;
        overflow-x: hidden;
        scrollbar-size-vertical: 1;
        scrollbar-background: transparent;
        scrollbar-background-hover: $surface;
        scrollbar-background-active: $surface;
        scrollbar-color: $panel;
        scrollbar-color-hover: $panel-lighten-1;
        scrollbar-color-active: $accent;
        scrollbar-corner-color: $surface;
    }

    #status {
        background: transparent;
        height: auto;
        margin: 0 2;
        display: none;
    }

    #prompt {
        dock: bottom;
        margin: 0 1 1 1;
        border: none;
        padding: 1 1;
        background: transparent;
        height: auto;
    }
    """

    BINDINGS = [('ctrl+c', 'quit', 'Quit')]

    def __init__(self, directory:str) -> None:
        super().__init__()
        self.directory = directory
        self._spinner = Spinner('dots', text=THINKING_TEXT, style=SYSTEM_COLOR)
        self._spinner_timer = None

    def compose(self) -> ComposeResult:
        yield RichLog(id='transcript', wrap=True, markup=True)
        yield Static(id='status')
        yield Input(placeholder=PLACEHOLDER, id='prompt')

    def on_mount(self) -> None:
        self.query_one('#transcript', RichLog).write(banner_text(self.directory))
        self.query_one('#prompt', Input).focus()

    def on_input_submitted(self, event:Input.Submitted) -> None:
        text = event.value.strip()
        event.input.value = ''
        if not text:
            return

        if text.startswith('/'):
            self._handle_command(text)
            return

        log = self.query_one('#transcript', RichLog)
        log.write(text)
        log.write('')
        self._start_thinking()
        self._send(text)

    def _handle_command(self, command:str) -> None:
        log = self.query_one('#transcript', RichLog)
        parts = command.strip().split(maxsplit=1)
        name = parts[0]

        if name in ('/exit', '/quit'):
            self.exit()
            return
        if name == '/help':
            log.write(help_text())
            log.write('')
            return
        if name == '/dir':
            if len(parts) < 2:
                log.write(error_line('Usage: /dir <path>'))
                log.write('')
                return
            new_directory = parts[1].strip()
            result = set_directory(new_directory)
            if result.startswith('Error'):
                log.write(error_line(result))
                log.write('')
                return
            self.directory = new_directory
            log.write(system_line('directory set to ' + new_directory))
            log.write('')
            return

        log.write(error_line('Unknown command: ' + name))
        log.write('')

    def _start_thinking(self) -> None:
        status = self.query_one('#status', Static)
        status.display = True
        self._spinner_timer = self.set_interval(1 / 12, self._tick_thinking)

    def _tick_thinking(self) -> None:
        self.query_one('#status', Static).update(self._spinner)

    def _stop_thinking(self) -> None:
        if self._spinner_timer is not None:
            self._spinner_timer.stop()
            self._spinner_timer = None
        self.query_one('#status', Static).display = False

    @work(thread=True)
    def _send(self, message:str) -> None:
        prompt = self.query_one('#prompt', Input)
        log = self.query_one('#transcript', RichLog)

        self.call_from_thread(setattr, prompt, 'disabled', True)

        response = send_message(message, self.directory)

        self.call_from_thread(self._stop_thinking)

        if response.startswith('Error'):
            self.call_from_thread(log.write, error_line(response))
        else:
            self.call_from_thread(log.write, assistant_body(response))
        self.call_from_thread(log.write, '')

        self.call_from_thread(setattr, prompt, 'disabled', False)
        self.call_from_thread(prompt.focus)
