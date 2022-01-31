#!/usr/bin/python3
# 9-rectangle.py
# Oscar Bedat <3961@holbertonschool.com>
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Define are recantgle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Print string
        """
        return '[Rectangle]' + str(self.__width) + '/' + str(self.__height)
