#!/usr/bin/env python

"""Test the hello_you module"""

from src.section6 import boolean


def test_can_main():
    """Test if main() function is implemented"""

    try:
        boolean.main()
    except AttributeError:
        # main() is not implemented.
        assert False
    except Exception:
        # We don't care if main() doesn't work, just that it exists.
        pass


def test_true_type():
    """Test true_type()."""

    assert boolean.true_type() == bool


def test_false_type():
    """Test true_type()."""

    assert boolean.false_type() == bool


def test_truthiness():
    """Test truthiness()."""

    assert boolean.truthiness()


def test_falseiness():
    """Test falseiness()."""

    assert boolean.falsiness()


def test_main():
    """Test main()."""

    boolean.main()
