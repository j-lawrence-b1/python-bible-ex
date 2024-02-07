#!/usr/bin/env python3

"""Module docstring. """


def main():
    output = ""
    # output now '1\n'
    output += f'{"hello".count("e")}\n'
    # output now '1\nhappy birthday\n'
    output += f'{"Happy Birthday".lower()}\n'
    # output now '1\nhappy birthday\nTO YOU\n'
    output += f'{"to you".upper()}\n'
    my_str = "wut"
    my_str.upper()
    # str.upper(), etc do not change string!
    # Output now '1\nhappy birthday\nTO YOU\nwut\n'
    output += f'{my_str}\n'
    # Output now '1\nhappy birthday\nTO YOU\nwut\nFoobar\n'
    output += f'{"foobar".capitalize()}\n'
    # str.capitalize() only works on the first word in the string.
    # Output now '1\nhappy birthday\nTO YOU\nwut\nFoobar\nFoo bar\n'
    output += f'{"foo bar".capitalize()}\n'
    # But str.title() does.
    # Output now '1\nhappy birthday\nTO YOU\nwut\nFoobar\nFoo bar\nFoo Bar'
    output += f'{"foo bar".title()}\n'
    # Output now '1\nhappy birthday\nTO YOU\nwut\nFoobar\nFoo bar\nFoo Bar\nTrue\nTrue\nTrue\nTrue\n'
    output += (
        f'{"FOO BAR".isupper()}\n{"foo bar".islower()}\n'
        + f'{"Foo Bar".istitle()}\n{"12345".isdecimal()}\n')
    # Etc.
    return output


if __name__ == "__main__":
    """
    Entry point.

    OPEN ISSUE' Should I upgrade to setuptools and setup.py?
    """

    print(main())
