#!/usr/bin/python3
# 9-rectangle.py
# Oscar Bedat <3961@holbertonschool.com>
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits
    from class 'BaseGeometry'
    Attributes:
    ----------
    width  {int} -- [Rectangle's width]
    height {int} -- [Rectangle's height]
    """

    def __init__(self, width, height):
        """
        private attributes width and height,
        and validating if they are ints.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
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
