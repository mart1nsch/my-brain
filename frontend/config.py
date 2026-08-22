import os


API_BASE_URL = os.environ.get('FRONTEND_API_URL', 'http://localhost:8008')
DEFAULT_DIRECTORY = os.environ.get('FRONTEND_DEFAULT_DIRECTORY', 'agent_creations')

ACCENT_COLOR = 'bold cyan'
SYSTEM_COLOR = 'dim white'
ERROR_COLOR = 'bold red'
