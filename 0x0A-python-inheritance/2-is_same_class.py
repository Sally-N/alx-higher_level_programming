#!/usr/bin/python3
"""Defines is_same_class module"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class
    args:
        obj (any): the object to check the instance for
        a_class (type): the class to compare the object with
    Returns:
        boolean: True if object is exactly an instance of the specified class
    """
    if type(obj) == a_class:
        return True
    else
        return False
