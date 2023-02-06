#!/usr/bin/python3
"""Defines an empty base_geometry module"""


class BaseGeometry:
    """empty class"""

    def area(self):
        """Empty area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        Args:
            name (str): The name
            value (int): The value
        """
        
        if type(value) != int:
            raise TypeError("{}must be an integer".format(name))
        if value <= 0:
            raise ValueError("{}must be greater then 0".format(name))
