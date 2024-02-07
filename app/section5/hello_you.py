#!/usr/bin/env python3

"""Module docstring. """


def prompt(ppt: str = "", default: str = "") -> str:
    """
    Prompt for console input.

    Keyword arguments:
    prompt -- Desired input hint (default: '').
    default -- Default input value (default: '').

    """

    retval = input(f"{ppt}? [{default}]: ")
    if retval is None:
        retval = default

    return retval.strip()


def main():
    name = None
    age = None
    city = None
    activity = None

    # Ask user for name.
    while not name:
        retval = prompt("What is your name")
        if len(retval) > 0:
            name = retval

    # Ask user for age.
    while not age:
        retval = prompt("What is your age")
        if retval.isnumeric():
            age = int(retval)

    # Ask user for city.
    while not city:
        retval = prompt("What city were you born in")
        if len(retval) > 0:
            city = retval

    # Ask user what they enjoy.
    while not activity:
        retval = prompt("What is your favorite activity")
        if len(retval) > 0:
            activity = retval

    # Create output text.
    output_text = (
        f"Hello, {name}. I see you are {age} years old, "
        + f"were born in {city}, and love {activity}."
    )

    # Print output to screen.
    return output_text


if __name__ == "__main__":
    """
    Entry point.

    OPEN ISSUE: Should I upgrade to setuptools and setup.py?
    """

    print(main())
