#!/usr/bin/python3
"""Defines inherits_from module"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a_class
    args:
        obj (any): the object to check
        a_class (type): the class to compare the object with
    Returns:
        boolean: True if obj is an instance of the a_class
    """

    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
