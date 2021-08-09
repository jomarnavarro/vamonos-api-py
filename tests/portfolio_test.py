import requests
from assertpy.assertpy import assert_that
from clients.login.login_client import LoginClient
from clients.portfolio.portolio_client import PortfolioClient

login_client = LoginClient()
portfolio_client = PortfolioClient()


def test_user_can_obtain_portfolio():
    login_res = login_client.valid_login()
    portfolio_res = portfolio_client.get_portfolio_auth(login_res)
    assert_that(portfolio_res.status_code).is_equal_to(requests.codes.ok)


def test_user_cant_obtain_portfolio_without_auth():
    portfolio_res = portfolio_client.get_portfolio_no_auth()
    assert_that(portfolio_res.status_code).is_equal_to(requests.codes.unauthorized)
