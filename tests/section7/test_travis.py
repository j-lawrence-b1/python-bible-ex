#!/usr/bin/env python

"""Test the travis module"""

"""Python imports."""
from io import StringIO

"""Application imports."""
from src.lib import console
from src.section7 import travis


def test_can_main():
    """Test if main() function is implemented"""

    try:
        travis.main()
    except AttributeError:
        # main() is not implemented.
        assert False
    except Exception:
        # We don't care if main() works, just that it exists.
        pass


def test_known_user(monkeypatch, capsys):
    """Test recognized name.

    Tested Dialog:
    --------------
    My name is Travis. Who are you? []: bob
    Hello, Bob!
    Would you like to be removed from the system? Pleaase enter Y[es] or N[o]? [N]: n
    No problem, I would hate to see you go.
    My name is Travis. Who are you? []: quit
    """

    inputs = StringIO("Bob\nn\nquit\n")
    # sys.capsys swallows the newline after the prompt.
    expected = (
        "My name is Travis. Who are you? []: Hello, Bob!\n"
        "Would you like to be removed from the system? Pleaase enter Y[es] or N[o]? [N]: No problem, I would hate to see you go.\n"
        "My name is Travis. Who are you? []: "
    )
    monkeypatch.setattr("sys.stdin", inputs)
    travis.main()
    captured = capsys.readouterr()
    assert captured.out == expected


def test_delete_user(monkeypatch, capsys):
    """Test recognized name.

    Tested Dialog:
    --------------
    My name is Travis. Who are you? []: bob
    Hello, Bob!
    Would you like to be removed from the system? Pleaase enter Y[es] or N[o]? [N]: y
    Removing user Bob.
    My name is Travis. Who are you? []: bob
    Would you like to be added to the system? Pleaase enter Y[es] or N[o]? [N]: n
    OK, maybe next time.
    My name is Travis. Who are you? []: quit
    """

    inputs = StringIO("Bob\ny\nquit\n")
    # sys.capsys swallows the newline after the prompt.
    expected = (
        "My name is Travis. Who are you? []: Hello, Bob!\n"
        "Would you like to be removed from the system? Pleaase enter Y[es] or N[o]? [N]: Removing user Bob.\n"
        "My name is Travis. Who are you? []: "
    )
    monkeypatch.setattr("sys.stdin", inputs)
    travis.main()
    captured = capsys.readouterr()
    assert captured.out == expected


def test_unknown_user(monkeypatch, capsys):
    """Test recognized name.

    Tested Dialog:
    --------------
    My name is Travis. Who are you? []: Carol
    Hmmm I don't think I have met you yet, Carol
    Would you like to be added to the system? Pleaase enter Y[es] or N[o]? [N]: n
    OK, maybe next time.
    My name is Travis. Who are you? []: quit
    """

    inputs = StringIO("Carol\nn\nquit\n")
    # sys.capsys swallows the newline after the prompt.
    expected = (
        "My name is Travis. Who are you? []: Hmmm I don't think I have met you yet, Carol\n"
        "Would you like to be added to the system? Pleaase enter Y[es] or N[o]? [N]: OK, maybe next time.\n"
        "My name is Travis. Who are you? []: "
    )
    monkeypatch.setattr("sys.stdin", inputs)
    travis.main()
    captured = capsys.readouterr()
    assert captured.out == expected


def test_add_user(monkeypatch, capsys):
    """Test recognized name.

    Tested Dialog:
    --------------
    My name is Travis. Who are you? []: Carol
    Hmmm I don't think I have met you yet, Carol
    Would you like to be added to the system? Pleaase enter Y[es] or N[o]? [N]: y
    Adding user Carol.
    My name is Travis. Who are you? []: Carol
    Hi, Carol! Would you like to be removed from the system? Pleaase enter Y[es] or N[o]? [N]: No problem, I would hate to see you go.\n"
    My name is Travis. Who are you? []: quit
    """

    inputs = StringIO("Carol\ny\nCarol\nn\nquit\n")
    # sys.capsys swallows the newline after the prompt.
    expected = (
        "My name is Travis. Who are you? []: Hmmm I don't think I have met you yet, Carol\n"
        "Would you like to be added to the system? Pleaase enter Y[es] or N[o]? [N]: Adding user Carol.\n"
        "My name is Travis. Who are you? []: Hello, Carol!\n"
        "Would you like to be removed from the system? Pleaase enter Y[es] or N[o]? [N]: No problem, I would hate to see you go.\n"
        "My name is Travis. Who are you? []: "
    )
    monkeypatch.setattr("sys.stdin", inputs)
    travis.main()
    captured = capsys.readouterr()
    assert captured.out == expected
