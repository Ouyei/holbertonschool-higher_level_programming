#!/usr/bin/python3
# 1-square.py
# Oscar Bedat <3965@holbertonschool.com>
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size):
        """__init__
        The __init__ method initializes the size value
        of the square.
        Attributes:
            size (int): The size of the square.
        """
        self.__size = size
