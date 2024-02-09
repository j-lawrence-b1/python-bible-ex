#!/usr/bin/env python

"""Test the email_slicer module"""

"""Import Python modules."""
from io import StringIO

"""Import Application modules."""
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


def test_get_email_success(monkeypatch):
    """Test success."""
    inputs = StringIO("some.body@example.com\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert email_slicer.get_email() == "some.body@example.com"


def test_get_email_eventual_success(monkeypatch):
    """Test success."""
    inputs = StringIO("some-bad-email-address\nsome.body@example.com\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert email_slicer.get_email() == "some.body@example.com"


def test_get_name():
    """Test extracting name from email."""
    assert email_slicer.get_name("some.body@example.com") == "some.body"


def test_get_domain():
    """Test extracting domain name from email."""
    assert email_slicer.get_domain("some.body@example.com") == "example.com"


def test_format_output():
    """Test constructing the output message."""
    assert email_slicer.format_output("some.body", "example.com") == (
        "Your name is some.body and your domain is example.com."
    )


def test_display_output(capsys):
    """Test printing the output message to the console."""
    msg = "Your name is some.body and your domain is example.com."
    email_slicer.display_output(msg)
    captured = capsys.readouterr()
    assert captured.out.strip() == msg


def test_main(monkeypatch, capsys):
    """Test if main() runs without error"""
    inputs = StringIO("some.body@example.com\n")
    # sys.capsys swallows the newline after the prompt.
    expected = "What is your email address? []: Your name is some.body and your domain is example.com.\n"
    monkeypatch.setattr("sys.stdin", inputs)
    email_slicer.main()
    captured = capsys.readouterr()
    assert captured.out == expected
