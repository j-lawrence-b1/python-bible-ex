#!/usr/bin/env python3

'''Module docstring. '''


def main():
    x = 'abcdefghijklmnopqrstuvwxyz'
    output = ''

    # First letter.
    # Output now 'a\n'
    output += f'{x[0]}\n'

    # Last letter.
    # Output now 'a\nz\n'
    output += f'{x[-1]}\n'

    # 3rd thru 6th chars. Note 3rd char is idx 2 and sixth char is idx 5.
    # Output now 'a\nz\ncdef\n'
    output += f'{x[2:6]}\n'

    # Last 3 chars.
    # Output now 'a\nz\ncdef\nxyz\n'
    output += f'{x[-3:]}\n'

    # Reverse the string with a slice.
    # Output now:
    #  'a\nz\ncdef\nxyz\n'
    #  + 'zyxwvutsrqponmlkjihgfedcba\n'
    output += f'{x[::-1]}\n'

    # Snip off first 5 chars.
    # Output now:
    #  'a\nz\ncdef\nxyz\n'
    #  + 'zyxwvutsrqponmlkjihgfedcba\nabcde\n'
    output += f'{x[:5]}\n'

    # Discard first 5 letters
    # Output now:
    #  'a\nz\ncdef\nxyz\n'
    #  + 'zyxwvutsrqponmlkjihgfedcba\nabcde\n'
    output += f'{x[5:]}\n'

    # snip off last 5 chars.
    # Output now:
    #  'a\nz\ncdef\nxyz\n'
    #  + 'zyxwvutsrqponmlkjihgfedcba\nabcde\n'
    #  + 'fghijklmnopqrstuvwxyz\nvwxyz\n'
    output += f'{x[-5:]}\n'

    # discard last 5 chars.
    # Output now:
    #  'a\nz\ncdef\nxyz\n'
    #  + 'zyxwvutsrqponmlkjihgfedcba\nabcde\n'
    #  + 'fghijklmnopqrstuvwxyz\nvwxyz\n'
    #  + 'abcdefghijklmnopqrstu\n'
    output += f'{x[:-5]}\n'

    return output


if __name__ == '__main__':
    '''
    Entry point.

    OPEN ISSUE' Should I upgrade to setuptools and setup.py?
    '''

    print(main())
