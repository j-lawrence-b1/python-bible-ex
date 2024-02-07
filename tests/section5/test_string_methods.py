#!/usr/bin/env python

'''Test the hello_you module'''

from app.section5 import string_methods


def test_can_main():
    try:
        string_methods.main()
    except AttributeError:
        assert False
    finally:
        assert True


def test_main():
    assert string_methods.main() == (
        '1\nhappy birthday\nTO YOU\nwut\nFoobar\nFoo bar\nFoo Bar\nTrue\nTrue\nTrue\nTrue\n')
