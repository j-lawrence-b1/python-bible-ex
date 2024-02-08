#!/usr/bin/env python

"""Utilities for getting and putting data to the console"""


def prompt(pmpt: str = "", dflt: str = "") -> str:
    """
    Prompt for console input.

    Keyword arguments:
    pmpt -- Desired input hint (default: '').
    dflt -- Default input value (default: '').

    Return:
    The input, as a stripped string, or ''.
    """

    retval = input(f"{pmpt}? [{dflt}]: ").strip()
    if retval == "":
        retval = dflt

    return retval
