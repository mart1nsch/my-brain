from frontend.config import API_BASE_URL, DEFAULT_DIRECTORY
from frontend.client import check_health
from frontend.app import AgentApp
from frontend.client import set_directory
import os


def main() -> None:
    if not check_health():
        print('Backend not reachable at ' + API_BASE_URL + '. Start it with: uvicorn main:app --reload --host 0.0.0.0 --port 8008')
        return

    set_directory(os.environ.get('USER_DIR'))
    AgentApp(DEFAULT_DIRECTORY).run()


if __name__ == '__main__':
    main()
