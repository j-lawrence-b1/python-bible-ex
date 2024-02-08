#!/usr/bin/env python3

'''The email_slicer project'''

'''Python imports'''
from sys import stderr
from pyisemail import is_email

'''Application imports'''
from src.lib import console


def get_email():
    '''Get user email address'''
    
    email = None
    while True:
        email = console.prompt('What is your email address')
        if is_email(email):
            break
        else:
            print("Please enter a valid email address", file=stderr)

    return email


def get_name(email: str):
    '''Slice out user name'''
    return email[:email.index('@')]


def get_domain(email: str):
    '''Slice out domain name'''
    return email[email.index('@')+1:]


def format_output(name: str, domain: str):
    '''Format message'''
    return "Your name is {} and your domain is {}.".format(name, domain)


def display_output(output: str):
    '''Display message'''
    print(output)


def main():
    '''The main thing'''

    email = get_email()
    name = get_name(email)
    domain = get_domain(email)
    output = format_output(name, domain)
    display_output(output)


if __name__ == '__main__':
    '''
    Entry point.

    OPEN ISSUE' Should I upgrade to setuptools and setup.py?
    '''

    main()
