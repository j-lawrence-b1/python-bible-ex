#!/usr/bin/env python

"""Test the hello_you module"""

from io import StringIO
from app.section5 import hello_you


def test_can_main():
    try:
        hello_you.main()
    except AttributeError:
        assert False
    finally:
        assert True


def test_prompt(monkeypatch):
    inputs = StringIO("San Francisco\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert hello_you.prompt("Enter City") == "San Francisco"


def test_main(monkeypatch):
    inputs = StringIO("Bobby\n3\nSF\ndiving\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert hello_you.main() == (
        "Hello, Bobby. I see you are 3 years old," +
        " were born in SF, and love diving."
    )
