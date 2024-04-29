#!/usr/bin/env python

"""Test the console module"""

from io import StringIO
from src.lib import console


def test_prompt(monkeypatch):
    """Test regular input"""

    inputs = StringIO("San Francisco\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert console.prompt("Enter City") == "San Francisco"


def test_prompt_user_default(monkeypatch):
    """Test user-provideddefault value"""

    inputs = StringIO("\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert console.prompt("Enter Yes/No", "Yes") == "Yes"


def test_prompt_builtin_default(monkeypatch):
    """Test built-in default value"""

    inputs = StringIO("\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert console.prompt("Something") == ""


def test_prompt_yn_yes(monkeypatch):
    """Test regular input"""

    inputs = StringIO("yes\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert console.prompt_yn("Do it") == True


def test_prompt_yn_YES(monkeypatch):
    """Test regular input"""

    inputs = StringIO("YES\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert console.prompt_yn("Do it") == True


def test_prompt_yn_no(monkeypatch):
    """Test regular input"""

    inputs = StringIO("no\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert console.prompt_yn("Do it") == False


def test_prompt_yn_NO(monkeypatch):
    """Test regular input"""

    inputs = StringIO("NO\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert console.prompt_yn("Do it") == False


def test_prompt_yn_user_default(monkeypatch):
    """Test user-provideddefault value"""

    inputs = StringIO("\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert console.prompt_yn("Do it", "Yes") == True


def test_prompt_yn_builtin_default(monkeypatch):
    """Test built-in default value"""

    inputs = StringIO("\n")
    monkeypatch.setattr("sys.stdin", inputs)
    assert console.prompt_yn("Do it") == False
