#!/usr/bin/python3
"""Module with a class that inherits from MyList class"""


class MyList(list):
    """A class that inherits from a base class"""
    def print_sorted(self):
        print(sorted(self))
