#!/usr/bin/env python

from src.section5 import hello_world


def test_can_main():
    try:
        hello_world.main()
    except AttributeError:
        assert False
    finally:
        assert True


def test_hello():
    assert hello_world.main() == "Hello, world!"
