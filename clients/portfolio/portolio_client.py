from clients.base_client import BaseClient
from config import portfolio_api_url
from utils.request import APIRequest
from utils.file_reader import read_file

class PortfolioClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.url = portfolio_api_url
        self.request = APIRequest()

    
    def get_portfolio_auth(self, login_res):
        self.headers['x-access-token'] = login_res.as_dict['token']
        return self.request.get(url=self.url, headers=self.headers)

    
    def get_portfolio_no_auth(self):
        self.headers = read_file('headers.json')
        return self.request.get(url=self.url, headers=self.headers)
