#!/usr/bin/env python

from app.section4 import health


def test_can_main():
    try:
        health.main()
    except NotImplementedError:
        assert False
    finally:
        assert True


def test_main_returns_valid_health_range(capsys):
    min_health = 49 + 25
    max_health = 49 + 50
    ret_val = health.main()
    ret_val = int(capsys.readouterr().out.strip())
    assert ret_val >= min_health and ret_val < max_health


def test_difficulty(capsys):
    """
    Test whether, on average, increased difficulty
    results in diminished health.
    """
    for outer in range(10):
        ret_val1 = 0
        ret_val2 = 0
        for inner in range(10):
            health.main(1)
            ret_val1 += int(capsys.readouterr().out.strip())
        for _ in range(10):
            health.main(2)
            ret_val2 += int(capsys.readouterr().out.strip())
        assert ret_val1 > ret_val2
