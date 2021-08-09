from json import dumps
from uuid import uuid4

from clients.base_client import BaseClient
from config import *
from utils.request import APIRequest
from utils.file_reader import read_file

class LoginClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.url = login_api_url
        self.request = APIRequest()

    def valid_login(self, body=None):
        if body is None:
            payload = read_file('credentials.json')
        else:
            payload = body

        print("PAY LOADDDDDD" + str(payload))
        
        response = self.request.post(self.url, dumps(payload), self.headers)
        return response

    def invalid_login(self, wrong_password):
        return self.request.post(self.url, dumps(wrong_password), self.headers)