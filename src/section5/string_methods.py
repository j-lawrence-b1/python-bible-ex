#!/usr/bin/env python3

"""Module docstring. """


def main():
    '''Demo various string methods'''

    output = ""

    # output now '1\n'
    output += f'{"hello".count("e")}\n'

    # NOTE: str.casefold() does the same thing as str.lower()
    # but works better with non-ascii encodings.
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

    # Detecting character classes.
    # Output now:
    # '1\nhappy birthday\nTO YOU\nwut\nFoobar\nFoo bar\n'
    # 'Foo Bar\nTrue\nTrue\nTrue\nTrue\n'
    output += (
        f'{"FOO BAR".isupper()}\n{"foo bar".islower()}\n'
        + f'{"Foo Bar".istitle()}\n{"12345".isdecimal()}\n')

    # Detecting/locating substrings.
    # Output now:
    # '1\nhappy birthday\nTO YOU\nwut\nFoobar\nFoo bar\n'
    # 'Foo Bar\nTrue\nTrue\nTrue\nTrue\n6\n'
    output += f'{"Happy Birthday".index('Birthday')}\n'

    # str.index() throws an exception if the substring isn't found.
    # Output now:
    # '1\nhappy birthday\nTO YOU\nwut\nFoobar\nFoo bar\n'
    # 'Foo Bar\nTrue\nTrue\nTrue\nTrue\n6\nwups!\n'
    try:
        'Happy Birthday'.index('foobar')
    except ValueError:
        output += 'wups!\n'

    # But str.find() does not.
    # Output now (
    #    '1\nhappy birthday\nTO YOU\nwut\nFoobar\n'
    #   + 'Foo bar\nFoo Bar\nTrue\nTrue\nTrue\nTrue\n6\nwups!\n-1\n'
    output += f'{"Happy Birthday".find("foobar")}\n'

    # Stripping leading and trailing characters.
    # Output now (
    #    '1\nhappy birthday\nTO YOU\nwut\nFoobar\n'
    #   + 'Foo bar\nFoo Bar\nTrue\nTrue\nTrue\nTrue\n6\nwups!\n-1\n'
    #   + 'foo\nfoo\nfoo\nfoo\n'
    output += (
        f'{" foo".lstrip()}\n{"foo ".rstrip()}\n'
        + f'{" foo ".strip()}\n{"0foo0".strip("0")}\n')
    return output


if __name__ == "__main__":
    """
    Entry point.

    OPEN ISSUE' Should I upgrade to setuptools and setup.py?
    """

    print(main())
