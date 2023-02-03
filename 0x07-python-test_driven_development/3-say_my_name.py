#!/usr/bin/python3
'''Defines a name-printing function'''


def say_my_name(first_name, last_name=""):
    '''
        Function that prints the first and last name passed to it
        Args:
            first_name (string): The first name
            last_name (string): The last name
    '''
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
