#!/usr/bin/env python3

"""T."""


def true_type():
    """The true_type function."""

    return type(True)


def false_type():
    """The false_type function."""

    return type(False)


def truthiness():
    """The truthiness function."""

    if True and 1 and "1" and [0] and {"key": 0}:
        return True
    else:
        return False


def falsiness():
    """The falsiness function."""

    if None or False or 0 or "" or [] or {}:
        return False
    else:
        return True


def main():
    """The main thing."""

    pass
