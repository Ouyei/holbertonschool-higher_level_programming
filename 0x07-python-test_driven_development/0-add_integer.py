#!/usr/bin/python3
# 0-add_integer.py
# Oscar Bedat <3961@holbertonschool.com>
"""" A module to add two numbers

This module performs the addition operation between two numbers,
these numbers can be integers or floats.

"""


def add_integer(a, b=98):
    """Returns the integer addition of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
