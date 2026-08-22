import requests
from frontend.config import API_BASE_URL


def check_health() -> bool:
    try:
        response = requests.get(API_BASE_URL + '/test', timeout=3)
        return response.status_code == 200
    except Exception:
        return False


def send_message(message:str, directory:str) -> str:
    try:
        response = requests.post(
            API_BASE_URL + '/message',
            json={ 'message': message, 'directory': directory },
            timeout=120
        )
        response.raise_for_status()
        return response.json()['message']
    except Exception as e:
        return 'Error: ' + str(e)


def get_directory() -> str:
    try:
        response = requests.get(API_BASE_URL + '/directory', timeout=10)
        response.raise_for_status()
        return response.json()['message']
    except Exception as e:
        return 'Error: ' + str(e)


def set_directory(directory:str) -> str:
    try:
        response = requests.post(
            API_BASE_URL + '/directory',
            json={ 'directory': directory },
            timeout=10
        )
        response.raise_for_status()
        return response.json()['response']
    except Exception as e:
        return 'Error: ' + str(e)
