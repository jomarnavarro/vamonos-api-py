import requests
from assertpy.assertpy import assert_that
from config import *
from utils.print_helpers import pretty_print
from utils.setup_helpers import *
from bs4 import BeautifulSoup

def test_user_quotes():
    token = login_succesful()
    headers = read_file('headers.json')
    headers['x-access-token'] = token
    payload = read_file('quote.json')
    quote_res = requests.post(quote_api_url, headers=headers, json=payload)
    assert_that(quote_res.status_code).is_equal_to(requests.codes.ok)
    assert_that('symbol' in quote_res.json())
    assert_that(quote_res.json()['symbol']).is_equal_to('IBM')
    assert_that('price' in quote_res.json())
    assert_that('name' in quote_res.json())

def test_cant_get_user_quotes_without_auth():
    headers = read_file('headers.json')
    payload = read_file('quote.json')
    quote_res = requests.post(quote_api_url, headers=headers, json=payload)
    assert_that(quote_res.status_code).is_equal_to(requests.codes.unauthorized)
    assert_that('error' in quote_res.json())


def test_quote_wrong_http_method():
    token = login_succesful()
    headers = read_file('headers.json')
    headers['x-access-token'] = token
    payload = read_file('quote.json')
    quote_res = requests.get(quote_api_url, headers=headers, json=payload)
    assert_that(quote_res.status_code).is_equal_to(requests.codes.not_allowed)
    assert_that('text/html' in quote_res.headers['Content-Type'])
    soup = BeautifulSoup(quote_res.text, 'html.parser')
    assert_that('Apology' in soup.title.text)
    assert_that('Method-Not-Allowed' in soup.img['src'])

    