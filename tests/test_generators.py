import pytest
from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator

@pytest.fixture
def transactions_list():
    return ([
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ])

def test_filter_by_currency_usd(transactions_list):
    transactions = transactions_list
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 3
    assert all(i['operationAmount']['currency']['code'] == 'USD' for i in result)


def test_filter_by_currency_rub(transactions_list):
    transactions = transactions_list
    result = list(filter_by_currency(transactions, "RUB"))
    assert len(result) == 2
    assert all(i['operationAmount']['currency']['code'] == 'RUB' for i in result)


@pytest.mark.parametrize('result, expected_len', [([], 0)])
def test_filter_by_currency_not_exist(transactions_list, expected_len, result):
    transactions = transactions_list
    assert len(result) == expected_len


@pytest.mark.parametrize('result, expected_len', [([], 0)])
def test_filter_by_currency_empty(result, expected_len):
    assert len(result) == expected_len


def test_transaction_descriptions(transactions_list):
    transactions = transactions_list
    result = list(transaction_descriptions(transactions))
    assert len(result) == len(transactions)


@pytest.mark.parametrize('result, expected_len', [([], 0)])
def test_transactions_descriptions_empty(result, expected_len):
    assert len(result) == expected_len


def test_card_number_generator():
    result = list(card_number_generator(1, 6))
    assert len(result) == 5


def test_card_number_generator_format():
    result = list(card_number_generator(1, 6))
    assert ' ' in result[1]
    assert len(result[2]) == 19


