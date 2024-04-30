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


def check_age(user_age, film_name):
    return True if user_age >= films[film_name][0] else False


def check_availability(film_name):
    return True if films[film_name][1] > 0 else False


def rent_film(film_name):
    films[film_name][1] -= 1


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
            if not check_age(age, choice):
                print("You are too young to view this film.")
                continue
            if not check_availability(choice):
                print("This film is currently unavailable.")
                continue
            rent_film(choice)
            print("Enjoy the film!")


if __name__ == "__main__":
    """Default function to run from the commandline."""
    main()
