#!/usr/bin/env python

'''Test the hello_you module'''

from app.section5 import email_slicer


def test_can_main():
    try:
        email_slicer.main()
    except AttributeError:
        assert False
    finally:
        assert True


def test_main():
    pass
