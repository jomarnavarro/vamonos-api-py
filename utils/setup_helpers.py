import os
import requests
from assertpy.assertpy import assert_that

from config import *
from utils.print_helpers import pretty_print


def login_succesful():
    login_res = requests.post(login_api_url, json = credentials)
    # pretty_print(login_res.json())
    assert_that(login_res.status_code).is_equal_to(requests.codes.ok)
    assert_that('token' in login_res.json())
    return login_res.json()['token']
