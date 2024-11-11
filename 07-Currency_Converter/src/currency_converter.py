import requests

def get_exchange_rate(base_currency: str, quote_currency: str) -> float:
    """Function for getting exchange rate using API

    :param base_currency: base currency 
    :param quote_currency: target currency
    :return: (quote_currency / base_currency)
    """
    url = f'https://open.er-api.com/v6/latest/{base_currency}'
    response = requests.get(url=url)
    if response.status_code != 200:
        return None
    return response.json()['rates'][quote_currency]


def convert_currency(amount: float, exchange_rate: float) -> float:
    """Function for calculating amount of money

    :param amount: amount of the money
    :param exchange_rate: exchange rate (quote_currency / base_currency)
    :return: amount of exchanged money
    """
    return amount * exchange_rate



if __name__ == '__main__':
    base_currency = input('Enter base currency: ')
    quote_currency = input('Enter quote currency: ')
    amount = float(input("Enter amount: "))
    exchange_rate = get_exchange_rate(base_currency, quote_currency)
    converted_amount = convert_currency(amount, exchange_rate)
    print(f'{amount} {base_currency} is {converted_amount} {quote_currency}')