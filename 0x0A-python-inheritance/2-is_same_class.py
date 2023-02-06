#!/usr/bin/python3
"""Module that contains is_same_class"""


def is_same_class(obj, a_class):
    """Checks if the oject is exactly an instance of the specified class
    args:
        obj (any): the object to check the instance for
        a_class (type): the class to compare the objet with
    Returns:
        boolean: True if object is exactly an instance of the specified class
    """
    if type(obj) == a_class:
        return True
    else
        return False
