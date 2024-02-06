#!/usr/bin/env python3

"""Module docstring. """


def prompt(prompt: str, default: str = None) -> str:
    """
    Prompt for console input.

    Keyword arguments:
    prompt -- Desired input hint.
    default -- Default input value
    """

    retval = input(f"{prompt} [{default}]: ")
    if input is None:
        retval = default

    return retval


# Ask user for name.

# Ask user for age.

# Ask user for city.

# Ask user what they enjoy.

# Create output text.

# Print output to screen.


def hello():
    """Say, 'Hello'."""

    return "Hello, world!"


def main():
    """The main thing."""

    return hello()


if __name__ == "__main__":
    """
    Entry point.

    OPEN ISSUE: Should I upgrade to setuptools and setup.py?
    """

    print(main())
