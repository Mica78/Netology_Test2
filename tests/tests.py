import unittest
import requests
from main import create_yadisk_folder
from dotenv import dotenv_values

TOKEN = dotenv_values("/home/mica78/Coding/Netology/Tests2/venv/.env")["TOKEN"]


class MyTestCase(unittest.TestCase):
    def test_create_folder_func(self):
        self.assertIn(create_yadisk_folder(
            url='https://cloud-api.yandex.net/v1/disk/resources/',
            folder_name='/Загрузки/Test'
        ),
            [200, 201, 409]
        )

    def test_presence_folder(self):
        self.assertEqual(
            requests.get(
                url='https://cloud-api.yandex.net/v1/disk/resources/',
                headers={'Authorization': f'OAuth {TOKEN}'},
                params={'path': '/Загрузки/Test'}
            ).status_code,
            200
        )


if __name__ == '__main__':
    unittest.main()
