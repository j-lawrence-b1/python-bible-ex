#!/usr/bin/env python

from app.section4 import health


def test_can_main():
    try:
        health.main()
    except AttributeError:
        assert False
    finally:
        assert True


def test_health(capsys):
    """
    Test whether health is returned within the min (25) and max(49) values.
    """
    min_health = 49 + 24
    max_health = 49 + 50
    ret_val = health.main()
    assert ret_val >= min_health and ret_val < max_health


def test_difficulty(capsys):
    """
    Test whether, on average, increased difficulty
    results in diminished health.
    """
    for _ in range(10):
        vals1 = [health.main(1) for _ in range(10)]
        vals2 = [health.main(2) for _ in range(10)]
        vals3 = [health.main(3) for _ in range(10)]
        assert sum(vals1) > sum(vals2) and sum(vals2) > sum(vals3)
