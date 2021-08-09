import requests
from assertpy.assertpy import assert_that
import pytest
from utils.file_reader import read_file
from clients.login.login_client import LoginClient

login_client = LoginClient()

def test_user_can_login(get_credentials):
    login_res = login_client.valid_login(get_credentials)
    assert_that(login_res.status_code).is_equal_to(requests.codes.ok)
    assert_that(login_res.as_dict).contains('token')


def test_invalid_password_login(wrong_password_credentials):
    login_res = login_client.invalid_login(wrong_password_credentials)
    assert_that(login_res.status_code).is_equal_to(requests.codes.unauthorized)
    assert_that(login_res.as_dict).contains('error')


def test_invalid_username_login(invalid_username_credentials):
    login_res = login_client.invalid_login(invalid_username_credentials)
    assert_that(login_res.status_code).is_equal_to(requests.codes.unauthorized)
    assert_that(login_res.as_dict).contains('error')


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