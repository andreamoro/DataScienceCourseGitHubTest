import pdb
import pytest
from datecalc import *
from datetime import date as dt, timedelta

# @pytest.fixture
# def today() -> datetime.date:
#     return dt.today()

# @pytest.fixture
# def yesterday(today) -> datetime.date:
#     return today + timedelta(days=-1)

# @pytest.fixture
# def tomorrow(today) -> datetime.date:
#     return today + timedelta(days=1)

def today() -> datetime.date:
    return dt.today()

def yesterday() -> datetime.date:
    return today() + timedelta(days=-1)

def tomorrow() -> datetime.date:
    return today() + timedelta(days=1)

@pytest.fixture
def raise_error():
    # pytest.fail(f"ERROR: {msg}")
    raise Exception(f"ERROR:")

# @pytest.mark.parametrize("start_date, end_date", [[today(), yesterday()], [yesterday(), today()]])
# def test_duration(start_date, end_date):
#     # This test aims to verify whether the day calculation
#     # returns a positive number 
#     # Using the pytest decorator I can run multiple tests at once.
#     assert duration(start_date, end_date) >= 0

# def test_futuredate(tomorrow):
#     # This test aims to verify whether the returned date is 
#     # greater than the input date.
#     assert when(tomorrow, 5) > tomorrow

def test_input_is_correct_format():
    # This test aims intentionally try to test for a string 
    # input that should be rejected, but do a controlled failure
    start_date = "2021-10-22"
    end_date = "2020-10-22"

    try:
        ret = duration(start_date, end_date)
    except Exception as e:
        # raise_error(e)
        # print("fuck")
        pytest.fail(f"The input data(s) is not in the expected format.\n{e}")
