import requests
from dotenv import dotenv_values

TOKEN = dotenv_values("/home/mica78/Coding/Netology/Tests2/venv/.env")["TOKEN"]


def create_yadisk_folder(url, folder_name, token=TOKEN):
    response = requests.put(
        url,
        headers={'Authorization': f'OAuth {token}'},
        params={'path': folder_name}
    )
    return response.status_code



