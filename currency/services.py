import requests


def latest_currency():
    url = "https://openexchangerates.org/api/latest.json?app_id=b39cc596779d4ce9ab445ae7d8ee67db"
    response = requests.get(url)
    data = response.json()
    rates = data["rates"]
    return rates


def historical_currency(date):
    url = "https://openexchangerates.org/api/historical/{date}.json?app_id=b39cc596779d4ce9ab445ae7d8ee67db".format(date=date)
    response = requests.get(url)
    data = response.json()
    rates = data["rates"]
    return rates


def calculate_currency(rates, lhs, rhs):
    lhs_val = rates[lhs]  # 1 USD
    rhs_val = rates[rhs]  # 1 USD
    return rhs_val / lhs_val
