#!/usr/bin/env python

'''Test the hello_you module'''

from app.section5 import slices


def test_can_main():
    try:
        slices.main()
    except AttributeError:
        assert False
    finally:
        assert True


def test_main():
    assert slices.main() == (
        'a\nz\ncdef\nxyz\n'
        + 'zyxwvutsrqponmlkjihgfedcba\nabcde\n'
        + 'fghijklmnopqrstuvwxyz\nvwxyz\n'
        + 'abcdefghijklmnopqrstu\n'
    )
