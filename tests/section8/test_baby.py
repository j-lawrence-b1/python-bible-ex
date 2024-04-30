#!/usr/bin/env python

"""Test the baby module"""

# Python imports.
from io import StringIO

# Application imports.
from src.lib import console
from src.section8 import baby

# Global variables.


def test_can_main():
    """Test if main() function is implemented"""

    try:
        baby.main()
    except AttributeError:
        # main() is not implemented.
        assert False
    except Exception:
        # We don't care if main() works, just that it exists.
        pass


def test_why(monkeypatch, capsys):
    """Test why.

    Tested Dialog:
    --------------
    Why? []:
    Because
    Why? quit
    Shaddup, already!
    Waahh!
    """

    inputs = StringIO("6\nquit\n")
    # sys.capsys swallows the newline after the prompt.
    expected = "Why? []: Why? []: Shaddup, already!\n" "Waahh!\n"
    monkeypatch.setattr("sys.stdin", inputs)
    baby.main()
    captured = capsys.readouterr()
    assert captured.out == expected
