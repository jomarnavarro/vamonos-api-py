import requests
from assertpy.assertpy import assert_that
from clients.login.login_client import LoginClient
from clients.quote.quote_client import QuoteClient

login_client = LoginClient()
quote_client = QuoteClient()


def test_user_quotes():
    login_res = login_client.valid_login()
    quote_res = quote_client.quote_auth(login_res)
    assert_that(quote_res.status_code).is_equal_to(requests.codes.ok)
    assert_that(quote_res.as_dict).contains('symbol')
    assert_that(quote_res.as_dict['symbol']).is_equal_to('IBM')
    assert_that(quote_res.as_dict).contains('price')
    assert_that(quote_res.as_dict).contains('name')


def test_cant_get_user_quotes_without_auth():
    quote_res = quote_client.quote_no_auth()
    assert_that(quote_res.status_code).is_equal_to(requests.codes.unauthorized)
    assert_that(quote_res.as_dict).contains('message')
    assert_that(quote_res.as_dict['message']).is_equal_to('Token is invalid')


def test_quote_wrong_http_method():
    login_res = login_client.valid_login()
    quote_res = quote_client.quote_wrong_method(login_res)
    assert_that(quote_res.status_code).is_equal_to(requests.codes.not_allowed)
    assert_that(quote_res.headers['Content-Type']).contains('text/html')
