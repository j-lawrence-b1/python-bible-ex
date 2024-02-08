#!/usr/bin/env python

"""Test the console module"""

from io import StringIO
from src.lib import console


def test_prompt(monkeypatch):
    '''Test regular input'''

    inputs = StringIO("San Francisco\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert console.prompt("Enter City") == "San Francisco"


def test_prompt_user_default(monkeypatch):
    '''Test user-provideddefault value'''

    inputs = StringIO("\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert console.prompt("Enter Yes/No", "Yes") == "Yes"


def test_prompt_builtin_default(monkeypatch):
    '''Test built-in default value'''

    inputs = StringIO("\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert console.prompt("Something") == ""
