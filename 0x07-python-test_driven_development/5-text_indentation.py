#!/usr/bin/python3
"""Defines a text-indentation funtion."""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    all_lines = [lines.strip(' ') for lines in text.split('\n')]
    new_text = "\n".join(all_lines)
    print(new_text, end="")
