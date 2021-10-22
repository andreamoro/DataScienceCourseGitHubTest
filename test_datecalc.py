import pytest
from datecalc import *
from datetime import date as dt, timedelta

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
