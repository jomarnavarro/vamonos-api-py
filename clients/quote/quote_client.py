from json import dumps

from bs4 import BeautifulSoup
from clients.base_client import BaseClient
from config import quote_api_url
from utils.request import APIRequest
from utils.file_reader import read_file

class QuoteClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.url = quote_api_url
        self.request = APIRequest()

    
    def quote_auth(self, login_res, body=None):
        if body is None:
            payload = read_file('quote.json')
        else:
            payload = body

        self.headers['x-access-token'] = login_res.as_dict['token']
        return self.request.post(self.url, dumps(payload), self.headers)

    def quote_no_auth(self, body=None):
        if body is None:
            payload = read_file('quote.json')
        else:
            payload = body
        
        self.headers = read_file('headers.json')
        return self.request.post(self.url, dumps(payload), self.headers)
    

    def quote_wrong_method(self, login_res):
        self.headers['x-access-token'] = login_res.as_dict['token']
        return self.request.get(self.url, self.headers)
