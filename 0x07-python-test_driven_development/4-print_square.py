#!/usr/bin/python3
# 4-print_square.py
# Oscar Bedat <3961@holbertonschool.com>
"""This module prints a square with the character '#'
of any positive integer size.
Example:
    ###
    ###
    ###
    * The size must be an integer greater than 0.
"""


def print_square(size):
    def print_square(size):
        """prints a square with "#"'s that has a length of size """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
