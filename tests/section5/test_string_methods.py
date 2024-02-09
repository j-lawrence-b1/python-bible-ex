#!/usr/bin/env python

"""Test the string_methods module"""

from src.section5 import string_methods


def test_can_main():
    """Test if main() function is implemented"""

    try:
        string_methods.main()
    except AttributeError:
        # main() is not implemented.
        assert False
    except Exception:
        # We don't care if main() doesn't work, just that it exists.
        pass


def test_main():
    assert string_methods.main() == (
        "1\nhappy birthday\nTO YOU\nwut\nFoobar\n"
        + "Foo bar\nFoo Bar\nTrue\nTrue\nTrue\nTrue\n6\nwups!\n-1\n"
        + "foo\nfoo\nfoo\nfoo\n"
    )
