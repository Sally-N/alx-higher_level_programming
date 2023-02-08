#!/usr/bin/python3


"""Defines the Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializer for Student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of an instance of Student"""
        new_dict = {}
        if attrs is not None:
            for k, v in self.__dict__.items():
                if k in attrs:
                    new_dict[k] = v
            return new_dict
        else:
            return self.__dict__
