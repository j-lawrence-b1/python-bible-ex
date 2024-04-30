#!/usr/bin/env python3

"""Module docstring."""

# Python imports

# Application imports
from src.lib import console

# Program defaults.

# Database of films -> minimum age, cost
films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Titanic": [12, 5],
    "Tarzan": [15, 5],
    "Ghost Busters": [12, 5],
}


def main():
    """The main thing."""

    age = int(console.prompt("How old are you"))

    while True:
        choice = console.prompt("What film would you like to watch").title()
        if choice == "Quit" or choice == "Bye":
            print("Goodbye!")
            break
        elif choice not in films:
            print("We don't have that film...")
        else:
            min_age = films[choice][0]
            num_seats = films[choice][1]
            if age < min_age:
                print("You are too young to view this film.")
                continue
            if num_seats < 1:
                print("This film is currently unavailable.")
                continue
            films[choice][1] -= 1
            print("Enjoy the film!")


if __name__ == "__main__":
    """Default function to run from the commandline."""
    main()
