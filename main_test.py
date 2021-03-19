#!/usr/bin/env python

from utils import greeting


def test_greeting():
    """test_greeting checks that greeting returns the correct message"""
    msg = greeting("John")
    want = "Hello John!"
    assert msg == want, f"the greeting is incorrect. Expected: {want} Actual: {msg}"


def run_tests():
    """run_tests runs all of the tests"""
    test_greeting()
    print("TESTS PASSED")


run_tests()
