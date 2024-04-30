#!/usr/bin/env python3

"""Module docstring."""

"""Python imports"""

"""Application imports"""
from src.lib import console

"""Program defaults."""
known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]


def main():
    """The main thing."""

    while True:
        name = console.prompt("My name is Travis. Who are you").casefold().capitalize()
        if not name:
            continue
        elif name == "Quit" or name == "Bye":
            break
        elif name in known_users:
            print(f"Hello, {name}!")
            if console.prompt_yn("Would you like to be removed from the system"):
                del_indexes = [
                    idx for idx, elem in enumerate(known_users) if elem == name
                ]
                for idx in del_indexes:
                    print(f"Removing user {known_users[idx]}.")
                    del known_users[idx]
            else:
                print("No problem, I would hate to see you go.")
        else:
            print(f"Hmmm I don't think I have met you yet, {name}")
            if console.prompt_yn("Would you like to be added to the system"):
                print(f"Adding user {name}.")
                known_users.append(name)
            else:
                print("OK, maybe next time.")


if __name__ == "__main__":
    main()
