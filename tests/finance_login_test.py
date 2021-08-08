import requests
from assertpy.assertpy import assert_that
import pytest


from config import *
from utils.print_helpers import pretty_print
from utils.file_reader import *


def test_user_can_login(get_credentials):
    login_res = requests.post(login_api_url, json=get_credentials)
    # pretty_print(login_res.json())
    assert_that(login_res.status_code).is_equal_to(requests.codes.ok)
    assert_that(login_res.json()).contains('token')
    pretty_print(login_res.json())


def test_invalid_password_login(wrong_password_credentials):
    login_res = requests.post(login_api_url, json=wrong_password_credentials)
    assert_that(login_res.status_code).is_equal_to(requests.codes.unauthorized)
    assert_that(login_res.json()).contains('error')


def test_invalid_username_login(invalid_username_credentials):
    login_res = requests.post(login_api_url, json=invalid_username_credentials)
    assert_that(login_res.status_code).is_equal_to(requests.codes.unauthorized)
    assert_that('error' in login_res.json())


@pytest.fixture
def get_credentials():
    yield read_file('credentials.json')


@pytest.fixture
def wrong_password_credentials():
    payload = read_file('credentials.json')
    payload['password'] = 'Pedroe'
    yield payload


@pytest.fixture
def invalid_username_credentials():
    payload = read_file('credentials.json')
    payload['username'] = 'invalid_username'
    yield payload