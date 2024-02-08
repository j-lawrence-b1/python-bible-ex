#!/usr/bin/env python

'''Test the string_methods module'''

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
            '1\nhappy birthday\nTO YOU\nwut\nFoobar\n'
            + 'Foo bar\nFoo Bar\nTrue\nTrue\nTrue\nTrue\n6\nwups!\n-1\n'
            + 'foo\nfoo\nfoo\nfoo\n'
    )
