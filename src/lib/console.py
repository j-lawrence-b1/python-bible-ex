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


def prompt_yn(pmpt: str = "Enter Y[es] or N[o]", dflt: str = "N") -> bool:
    """
    Prompt for a yes or no answer.

    Keyword arguments:
    pmpt -- Desired input hint (default: \"Enter Y[es] or N[o]\"').
    dflt -- Default input value (default: \"N\").

    Return:
    bool(True), if input begins with "Y" or "y", else False.
    """
    return (
        True
        if prompt(f"{pmpt}? Pleaase enter Y[es] or N[o]", dflt).upper().startswith("Y")
        else False
    )
