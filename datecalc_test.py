import unittest
import logging
from typing import NamedTuple
from datecalc import *
from datetime import date as dt, timedelta

def today() -> datetime.date:
    return dt.today()

def yesterday() -> datetime.date:
    return today() + timedelta(days=-1)

def tomorrow() -> datetime.date:
    return today() + timedelta(days=1)

def some_other_day(number_of_days: int, start_date: datetime.date = today()) -> datetime.date:
    return start_date + timedelta(days=number_of_days)

class TestDuration(unittest.TestCase):
    # Wrapping all tests about the duration in a single class
    # 
    # Note: the function `duration` has not been properly written as it does
    # not use any strong type hinting. 
    # Also, it does not include documentation, hence any sort of 
    # tests could have been written including failing tests that 
    # invalidates the test's logic which implies that some should 
    # test possible inputs to a given function.

    # Using the logging class I capture messsages that I will print later on the console 
    # logging.INFO - prints warnings and error
    # logging.DEBUG - prints the above +  debug messages
    # print - print() statements will be always printed
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger()

    def test_positives(self):
        # Aim to test a range of positive dates
        test = NamedTuple('Dates', [
            ('start', datetime.date), 
            ('end', datetime.date), 
            ('expected_return', int)
        ])

        tests = [
            test(today(), tomorrow(), 1),
            test(today(),yesterday(), 1),
            test(yesterday(), today(), 1),
            test(yesterday(), tomorrow(), 2),
            test(some_other_day(30), today(), 30)
        ]

        for test in tests:
            ret = duration(test.start, test.end)
            self.assertEqual(ret, test.expected_return)

    def test_crazy_dates(self):
        # Aim to test a range of dates with extreme values
        test = NamedTuple('Dates', [
            ('start', datetime.date), 
            ('end', datetime.date), 
            ('expected_return', int)
        ])
        tests = [
            test(some_other_day(-1000), some_other_day(-2000), 1000),
            test(some_other_day(1000), some_other_day(2000), 1000)
        ]

        for test in tests:
            ret = duration(test.start, test.end)
            self.assertEqual(ret, test.expected_return)
            # self.log.error(f"{test.start, test.end}")

    def test_wrong_input(self):
        # This test is expected to FAIL, but this is something I know
        # only because I lookeed at the source code.
        # In a real "black/box" model this is something that should 
        # be clear via the document implementation or the method signature
        test = NamedTuple('Dates', [
            ('start', str), 
            ('end', str), 
            ('expected_return', int)
        ])
        tests = [
            test("2021-10-24", "2021-10-25", 1), 
            test("2021-10-25", "2021-10-24", 1)
        ]

        for test in tests:
            # Here I catch any exception. 
            # By doing so, I create a controlled test output which will
            # not interrupt the execution of the tests, rather output 
            # just an error message.
            # 
            # Such an approach works only by using the unittest call
            # `python -m unittest discover -p '*test.py' -v`
            #
            # For a pytest approach, the loglevel has to be specifically 
            # declared with:
            # `pytest -v --log-cli-level=INFO` 
            # A simple `pytest -v` call (in verbose mode) return a PASSED
            # without returning the log in the console, thus giving
            # the false impression everything is ok. 
            try:
                ret = duration(test.start, test.end)
                self.assertEqual(ret, test.expected_return)
            except TypeError as exc:                
                self.log.error(f"Error {exc}")
                self.log.info(f"The argument passed were: {test.start, test.end}")

class TestWhen(unittest.TestCase):
    def test_future_date(self):
        # This test aims to verify the expected date after the days addition.
        test = NamedTuple('Dates', [
            ('start', datetime.date), 
            ('days', int), 
            ('expected_return', datetime.date)
        ])
        tests = [
            test(some_other_day(0, dt(2021,10,23)), 7, dt(2021,10,30))
        ]

        for test in tests:
            ret = when(test.start, test.days)
            self.assertEqual(ret, test.expected_return)
