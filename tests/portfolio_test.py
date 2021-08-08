from json import dumps
from uuid import uuid4
import os

import requests
from assertpy.assertpy import assert_that

# from utils.print_helpers import pretty_print
from config import *
from utils.print_helpers import pretty_print
from utils.file_reader import *
from utils.setup_helpers import login_succesful
import pytest

def test_user_can_obtain_portfolio():
    token = login_succesful()
    headers['x-access-token'] = token
    portfolio_res = requests.get(portfolio_api_url, headers=headers)
    assert_that(portfolio_res.status_code).is_equal_to(requests.codes.ok)


def test_user_cant_obtain_portfolio_without_auth():
    headers['x-access-token'] = 'undefined'
    portfolio_res = requests.get(portfolio_api_url, headers=headers)
    assert_that(portfolio_res.status_code).is_equal_to(requests.codes.unauthorized)

