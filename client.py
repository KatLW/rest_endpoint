import logging

import requests
from requests.exceptions import HTTPError


class HttpClient:

    def __init__(self):
        self.base_url = 'http://localhost:5000/'
        self.headers = {
            'Content-Type': 'application/json'
        }

    def send_http_request(self, data, endpoint='total'):
        url = self.base_url + endpoint
        numbers = self.format_numbers_list(data)
        try:
            response = requests.post(url=url, json=numbers, headers=self.headers)
            if response.status_code == 200:
                return response.json()
            response.raise_for_status()
        except HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')
        except Exception as error:
            logging.error(f'Exception occurred when sending request! Error: {error}')

    @staticmethod
    def format_numbers_list(numbers: list) -> dict:
        return {
            'numbers': numbers
        }


if __name__ == '__main__':
    http_client = HttpClient()
    print(http_client.send_http_request([1, 2, 3, 4, 5]))

    numbers_to_add = list(range(10000001))
    print(http_client.send_http_request(numbers_to_add))
