#!/usr/bin/python3
# 7-base_geometry.py
# Oscar Bedat <3961@holbertonschool.com>
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent a base geometry"""

    def area(self):
        """area: return area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates value
        Arguments:
            name {str} -- name of an instance
            value {int} -- type of instance
        Raises:
            TypeError: [must be an integer]
            ValueError: [must be greater than 0]
        """
        if type(value) != int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
