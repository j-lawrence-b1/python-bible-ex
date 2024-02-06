#!/usr/bin/env python

from app.section5 import hello_you


class TestsHelloYou:
    """Test the hello_you module"""

    def test_can_main():
        try:
            hello_you.main()
        except AttributeError:
            assert False
        finally:
            assert True

    def test_prompt(mocker):
        with mocker.patch.object(__builtins__, "input", lambda: "San Francisco"):
            assert hello_you.prompt("Enter City") == "San Franciscox"

    def test_main():
        assert False
