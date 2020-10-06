import logging

import requests
from requests.exceptions import HTTPError


class HttpProvider:
    def __init__(self):
        self.url = 'http://localhost:5000'
        self.headers = {'Content-Type': 'application/json'}

    def send_post_request(self, data, suffix='/total'):
        endpoint = self.url + suffix
        try:
            response = requests.post(url=endpoint, json=data, headers=self.headers)
            if response.status_code == '200':
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
    http_provider = HttpProvider()

    nums = http_provider.format_numbers_list([1, 2, 3, 4, 5])
    print(nums)
    result = http_provider.send_post_request(nums)
    print(result)
