#!/usr/bin/python3
# 4-print_square.py
# Oscar Bedat <3961@holbertonschool.com>
"""
This is the "4-print_square" module.
The 4-print_square  module supplies one function, print_square(size).
"""


def print_square(size):
    """
    Prints the names
    Args:
        size (int): The size of the square to prints.
    Raises:
        TypeError: If `size` isn't integer.
        ValueError: If `size` is less than 0.
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print('#', end='')

            if j % size == 0 and j > 0:
                print()
