#!/usr/bin/python3
# 6-square.py
# Oscar Bedat <3961@holbertonschool.com>
"""Define a class Square."""


class Square:
    """class variable size"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize new square"""
        self.__size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """class variable size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets position"""

        if type(value) is not tuple or len(value) > 1:
            raise TypeError("position must be a tumple of two positive int")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square with the # char"""
        position = self.position[0]
        size = self.size
        [print('\n', end='') for _ in range(self.position[1])]

        fot _ in range(self.size):
            for _ in range(position):
                print(' ', end='')
            print(size * '#')
