#!/usr/bin/python3
# 3-is_kind_of_class.py
# Oscar Bedat <3961@holbertonschool.com>
"""Defines a class adn inherited class_checking function."""


def is_kind_of_class(obj, a_class):
    """
    Checks if `obj` is the same class or inherit from `a_class`
    Args:
        obj (any): The object to compare
        a_class (any): The class to compare with the object
    Returns:
        `True` if the object is an instance or inherit from the
        specified class; otherwise `False`
    """

    if isinstance(obj, a_class):
        return True
    return False
