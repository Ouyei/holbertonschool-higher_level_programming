#!/usr/bin/python3
# 100-my_int.py
# Oscar Bedat <3961@holbertonschool.com>
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """ my int class"""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
