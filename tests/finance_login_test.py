from json import dumps
from uuid import uuid4
import os

import requests
from assertpy.assertpy import assert_that

from config import *
from utils.print_helpers import pretty_print

def test_user_can_login():
    login_res = requests.post(login_api_url, json=credentials)
    # pretty_print(login_res.json())
    assert_that(login_res.status_code).is_equal_to(requests.codes.ok)
    assert_that('token' in login_res.json())
    pretty_print(login_res.json())

def test_invalid_password_login():
    login_res = requests.post(login_api_url, json=invalid_password_credentials)
    assert_that(login_res.status_code).is_equal_to(requests.codes.unauthorized)
    assert_that('error' in login_res.json())


def test_invalid_username_login():
    login_res = requests.post(login_api_url, json=invalid_username_credentials)
    assert_that(login_res.status_code).is_equal_to(requests.codes.unauthorized)
    assert_that('error' in login_res.json())
