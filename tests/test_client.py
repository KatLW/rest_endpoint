import json
from unittest import TestCase
import mock
import requests
from requests.exceptions import HTTPError

from client import HttpClient
from tests import test_data


class MockResponse(mock.MagicMock):

    def __init__(self, status_code, data_dict):
        super(MockResponse, self).__init__(status_code)
        self.code = status_code
        self.data = data_dict

    @property
    def status_code(self):
        return self.code

    def json(self):
        return json.dumps({
            'status_code': self.status_code,
            'data': self.data
        })

    def raise_for_status(self):
        raise requests.exceptions.RequestException


class TestHttpClient(TestCase):

    def setUp(self) -> None:
        self.http_client = HttpClient()
        self.data = test_data.nums
        self.numbers = self.http_client.format_numbers_list(self.data)

    def test_send_post_request_successful(self):
        expected = {'status_code': 200, 'data': {'total': sum(self.data)}}
        with mock.patch('requests.post', return_value=MockResponse(200, {'total': sum(self.data)})):
            result = self.http_client.send_http_request(self.numbers)

        self.assertEqual(json.dumps(expected), result)

    def test_http_error_response(self):
        with mock.patch('requests.post', return_value=MockResponse(404, None)):
            result = self.http_client.send_http_request(self.numbers)

            self.assertIsNone(result)

    def test_http_request_exceptions(self):
        with self.assertRaises(Exception) as context:
            result = self.http_client.send_http_request()

            self.assertTrue(context.exception)
            self.assertIsNone(result)
