#!/usr/bin/env python

"""Test the hello_you module"""

from io import StringIO
from src.section5 import hello_you


def test_main(monkeypatch):
    inputs = StringIO("Bobby\n3\nSF\ndiving\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert hello_you.main() == (
        "Hello, Bobby. I see you are 3 years old," +
        " were born in SF, and love diving."
    )
