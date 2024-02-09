#!/usr/bin/env python

from src.section5 import hello_world


def test_can_main():
    """Test if main() function is implemented"""

    try:
        hello_world.main()
    except AttributeError:
        # main() is not implemented.
        assert False
    except Exception:
        # We don't care if main() doesn't work, just that it exists.
        pass


def test_hello():
    assert hello_world.main() == "Hello, world!"
