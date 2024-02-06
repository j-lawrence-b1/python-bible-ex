#!/usr/bin/env python

from app.section5 import hello_you


def test_can_main():
    try:
        hello_you.main()
    except AttributeError:
        assert False
    finally:
        assert True


def test_hello():
    pass
