#!/usr/bin/python3
# 2-matrix_divided.py
# Oscar Bedat <3961@holbertonschool.com>
"""A module to divides all elements of a matrix.
This module is in charge of dividing all the values of a matrix
according to a divisor given by the user. For the program to work
properly, the following aspects must be taken into account:
    * The matrix must  must be a list of lists of integers or floats.
    * Each row of the matrix must be of the same size.
    * The divisor must be a number (integer or float) other than 0.
    * The division of all elements of the matrix is rounded off
    to 2 decimal places.
    * The result is delivered in a new matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.
    This function takes the data sent by the user to verify
    that the matrix contains lists within it and that each
    list contains integer or floating type numbers.
    The result of the splitting operation is then added to a
    new list in a new matrix with the same matrix structure
    given by the user.
    In case the format of the matrix is incorrect
    or the divisor is not a number, this function
    will raise an error.
    Args:
        matrix (:obj:`list` of :obj:`list`): The matrix to be divided.
        div (int): The divisor number.
    Returns:
        list: A new matrix with all elements divided.
    Raises:
        TypeError: If `matrix` list of lists of integers or floats or
            if `div` is not a number.
        ZeroDivisionError: If `div` is equal to `0`.
    """
    size = None
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for l in matrix:
        if type(l) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(l)
        elif size != len(l):
            raise TypeError("Each row of the matrix must have the same size")
        for i in l:
            if type(i) is not int and type(i) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in l] for l in matrix]
