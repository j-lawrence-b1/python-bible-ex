#!/usr/bin/env python

"""Test the cinema module"""

"""Python imports."""
from io import StringIO

"""Application imports."""
from src.lib import console
from src.section7 import cinema


def test_can_main():
    """Test if main() function is implemented"""

    try:
        cinema.main()
    except AttributeError:
        # main() is not implemented.
        assert False
    except Exception:
        # We don't care if main() works, just that it exists.
        pass


def test_quit(monkeypatch, capsys):
    """Test recognized name.

    Tested Dialog: Enter age then quit
    -----------------------------------
    How old are you? []: 6
    What film would you like to watch? []: quit
    Goodbye!
    """

    inputs = StringIO("6\nquit\n")
    # sys.capsys swallows the newline after the prompt.
    expected = "How old are you? []: What film would you like to watch? []: Goodbye!\n"
    monkeypatch.setattr("sys.stdin", inputs)
    cinema.main()
    captured = capsys.readouterr()
    assert captured.out == expected


def test_unknown_film(monkeypatch, capsys):
    """Test recognized name.

    Tested Dialog: Enter age then quit
    -----------------------------------
    How old are you? []: 6
    What film would you like to watch? []: Booboo the Bear
    We don't have that film...
    What film would you like to watch? []: quit
    Goodbye!
    """

    inputs = StringIO("6\nBooboo the Bear\nquit\n")
    # sys.capsys swallows the newline after the prompt.
    expected = (
        "How old are you? []: What film would you like to watch? []: We don't have that film...\n"
        "What film would you like to watch? []: Goodbye!\n"
    )
    monkeypatch.setattr("sys.stdin", inputs)
    cinema.main()
    captured = capsys.readouterr()
    assert captured.out == expected


def test_unknown_film(monkeypatch, capsys):
    """Test recognized name.

    Tested Dialog: Enter age then quit
    -----------------------------------
    How old are you? []: 6
    What film would you like to watch? []: Booboo the Bear
    We don't have that film...
    What film would you like to watch? []: quit
    Goodbye!
    """

    inputs = StringIO("6\nBooboo the Bear\nquit\n")
    # sys.capsys swallows the newline after the prompt.
    expected = (
        "How old are you? []: What film would you like to watch? []: We don't have that film...\n"
        "What film would you like to watch? []: Goodbye!\n"
    )
    monkeypatch.setattr("sys.stdin", inputs)
    cinema.main()
    captured = capsys.readouterr()
    assert captured.out == expected
