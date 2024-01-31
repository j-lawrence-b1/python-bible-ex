#!/usr/bin/env python

from app.section4 import health


def test_main_does_not_crash():
    health.main()
    assert True


def test_main_returns_valid_health_range(capsys):
    min_health = 49 + 25
    max_health = 49 + 50
    ret_val = health.main()
    ret_val = int(capsys.readouterr().out.strip())
    assert ret_val >= min_health and ret_val < max_health
