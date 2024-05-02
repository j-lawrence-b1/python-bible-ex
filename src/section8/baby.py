#!/usr/bin/env python3

"""Module docstring."""

# Python imports
from random import randint

# Application imports
from src.lib import console

# Global variables.
questions = [
    "Why is the sky blue",
    "Why is the earth round",
    "Why do the clouds float in the sky",
    "why is the grass green",
    "Why is there a face on the moon",
    "Where did all the dinosaurs go",
]


def main():
    """The main thing."""

    while True:
        answer = console.prompt(questions[randint(0, len(questions)) - 1]).lower()
        if answer == "just because":
            break
    print("Waahh!")


if __name__ == "__main__":
    """Default function to run from the commandline."""
    main()
