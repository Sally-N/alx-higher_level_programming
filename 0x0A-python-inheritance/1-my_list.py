#!/usr/bin/python3
"""Module with a class that inherits from another class"""


class MyList(list):
    """Prints the list in sorted order"""
    def print_sorted(self):
        list.sort()
    return list
