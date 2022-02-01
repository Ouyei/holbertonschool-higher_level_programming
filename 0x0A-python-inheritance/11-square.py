#!/usr/bin/python3
# 11-square.py
# Oscar Bedat <3961@holbertonschool.com>
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square - Multiple inheritance
    """

    def __init__(self, size):
        """
        Initialize a new square.
        Args:
        size (int): The size of the new square.
        """

        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return '[Square]' + str(self.__size) + '/' + str(self.__size)
