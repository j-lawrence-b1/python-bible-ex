#!/usr/bin/env python

"""Test the email_slicer module"""

from src.section5 import email_slicer


def test_can_main():
    """Test if main() function is implemented"""

    try:
        email_slicer.main()
    except AttributeError:
        # main() is not implemented.
        assert False
    except Exception:
        # We don't care if main() doesn't work, just that it exists.
        pass


def test_main():
    """Test if main() runs without error"""

    email_slicer.main()
