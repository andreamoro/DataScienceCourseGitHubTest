import pytest
from datecalc import *
from datetime import date as dt, timedelta

@pytest.fixture
def today() -> datetime.date:
    return dt.today()

@pytest.fixture
def yesterday(today) -> datetime.date:
    return today + timedelta(days=-1)

@pytest.fixture
def tomorrow(today) -> datetime.date:
    return today + timedelta(days=1)

def test_duration(today, yesterday):
    # This test aims to verify whether the calculator refuse an 
    # ending date past the start date.
    #
    # It is expected to fail
    assert duration(today, yesterday) < 0

def test_futuredate(tomorrow):
    # This test aims to verify whether the returned date is 
    # greater than the input date.
    #
    # It is expect to succeed
    assert when(tomorrow, 5) > tomorrow