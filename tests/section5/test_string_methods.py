#!/usr/bin/env python

"""Test the hello_you module"""

from app.section5 import string_methods


def test_can_main():
    try:
        string_methods.main()
    except AttributeError:
        assert False
    finally:
        assert True
