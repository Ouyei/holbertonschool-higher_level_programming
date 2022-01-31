#!/usr/bin/python3
# 4-inherits_from.py
# Oscar Bedat <3961@holbertonschool.com>
"""Defines an inherited class_checking function."""


def inherits_from(obj, a_class):
    """
    inherits_from: returns True if the
    object is an instance of a class that inherited
    (directly or indirectly) from the specified class ;
    otherwise False.
    Args:
        obj: object
        a_class: class
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
