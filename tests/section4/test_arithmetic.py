#!/usr/bin/env python3

from src.section4 import arithmetic


def test_can_add():
    """Test whether the main() function exists."""
    try:
        arithmetic.add()
    except AttributeError:
        # main() is not implemented.
        assert False
    except Exception:
        # Capture all other errors. We just care that it exists.
        pass


def test_add():
    assert arithmetic.add(2, 2) == 4
    assert arithmetic.add(2, 2.2) == 4.2


def test_promotion():
    assert type(arithmetic.add(2, 2.0)) == float


def test_precedance():
    # B O D M A S
    assert 2 * 2 + 1 == 5  # Brackets trump Order
    assert 2 * (2 + 1) == 6  # Multiplcation has precedence over addition
    assert 1 + 2 * 2 == 5  # even if the order is switched
    assert 1 + 2 * 2 == 5
