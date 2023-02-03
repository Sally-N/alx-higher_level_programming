#!/usr/bin/python3
"""Defines a text-indentation funtion."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after specified characters `.`, `?` & `:`
    Args:
        text(str): text to be printed.
    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
