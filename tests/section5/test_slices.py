#!/usr/bin/env python

"""Test the hello_you module"""

from src.section5 import slices


def test_can_main():
    """Test if main() function is implemented"""

    try:
        slices.main()
    except AttributeError:
        # main() is not implemented.
        assert False
    except Exception:
        # We don't care if main() doesn't work, just that it exists.
        pass


def test_main():
    assert slices.main() == (
        "a\nz\ncdef\nxyz\n"
        + "zyxwvutsrqponmlkjihgfedcba\nabcde\n"
        + "fghijklmnopqrstuvwxyz\nvwxyz\n"
        + "abcdefghijklmnopqrstu\n"
    )
