#!/usr/bin/python3
"""Defines is_kind_of_class module"""

def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class
    args:
        obj (any): the object to check
        a_class (type): the class to compare the object with
    Returns:
        boolean: True if obj is an instance of the a_class
    """

    if isinstance(obj, a_class):
        return True
    return False
