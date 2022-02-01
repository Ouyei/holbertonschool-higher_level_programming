#!/usr/bin/python3
# 9-student.py
# Oscar Bedat <3961@holbertonschool.com>
"""Defines a class Student."""


class Student:
    """Represent a student."""
    def __init__(self, first_name, last_name, age):
        """__init__ initialized constructor
        Args:
            first_name (str): first name
            last_name (str: last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
