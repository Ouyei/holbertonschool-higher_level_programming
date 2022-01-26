#!/usr/bin/python3
# 101-locked_class.py
# Oscar Bedat <3961@holbertonschool.com>
class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
