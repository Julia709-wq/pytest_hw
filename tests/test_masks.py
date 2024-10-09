from src.masks import get_mask_card_number, get_mask_account
import pytest


@pytest.fixture
def card_number():
    return 7000792289606361


@pytest.fixture
def account_number():
    return 73654108430135874305


def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == '7000 79** **** 6361'


def test_get_mask_account():
    assert get_mask_account(73654108430135874305) == '**4305'
