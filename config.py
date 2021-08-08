# base urls
url = 'http://localhost:5000'
api = f'{url}/api'

login_endpoint = '/login'
portfolio_endpoint = '/portfolio'
quote_endpoint = '/quote'
buy_endpoint = '/buy'
sell_endpoint = '/sell'
history_endpoint = '/history'

login_api_url = api + login_endpoint
portfolio_api_url = api + portfolio_endpoint
quote_api_url = api + quote_endpoint
buy_api_url = api + buy_endpoint
sell_api_url = api + sell_endpoint
history_api_url = api + history_endpoint

credentials = {'username': 'Pedro', 'password': 'Pedro'}

invalid_password_credentials = {'username': 'Pedro', 'password': 'Pedroe'}

invalid_username_credentials = {'username': 'invalid', 'password': 'Pedro'}

headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-access-token': 'placeholder'
}

invalid_token_headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-access-token': 'placeholder'
}