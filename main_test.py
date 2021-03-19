#!/usr/bin/env python

from main import greeting


def test_greeting():
    msg = greeting()
    want = "hello there!"
    assert msg == want, f"the greeting is incorrect. Expected: {want} Actual: {msg}"


def run_tests():
    test_greeting()


run_tests()
