#!/usr/bin/env python

from src.section4 import maths


def test_round_is_int():
    assert type(maths.round(4.5)) == int


def test_round_down():
    assert maths.round(4.9999999) == 4


def test_round_up():
    assert maths.round(5.0) == 5
