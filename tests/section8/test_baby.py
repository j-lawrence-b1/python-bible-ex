#!/usr/bin/env python

"""Test the baby module"""

# Python imports.
from io import StringIO
import re

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
    """Test just because.

    Tested Dialog:
    --------------
    Why <something>? []:
    just because
    Waahh!
    """

    inputs = StringIO("just because\n")
    # sys.capsys swallows the newline after the prompt.
    # Using a regex because questions are random.
    expected_regex = re.compile("^Why([^?]+)\? \[\]: Waahh\!\n$")
    monkeypatch.setattr("sys.stdin", inputs)
    baby.main()
    captured = capsys.readouterr()
    assert expected_regex.search(captured.out).group() == captured.out
