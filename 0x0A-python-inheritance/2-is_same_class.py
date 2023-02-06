#!/usr/bin/python3
"""Defines is_same_class module"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of a_class
    args:
        obj (any): the object to check
        a_class (type): the class to compare the object with
    Returns:
        boolean: True if obj is an instance of the a_class
    """

    if type(obj) == a_class:
        return True
    return False
