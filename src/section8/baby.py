#!/usr/bin/env python3

"""Module docstring."""

# Python imports

# Application imports
from src.lib import console

# Global variables.


def main():
    """The main thing."""

    while True:
        answer = console.prompt("Why")
        if answer == "quit" or answer == "bye":
            print("Shaddup, already!")
            print("Waahh!")
            break


if __name__ == "__main__":
    """Default function to run from the commandline."""
    main()
