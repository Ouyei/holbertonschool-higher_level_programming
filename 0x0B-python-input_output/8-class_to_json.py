#!/usr/bin/python3
# 8-class_to_json.py
# Oscar Bedat <3961@holbertonschool.com>
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """class_to_json return dictionary description with simple data structure
    Args:
        obj : any object for example list, dict
    """
    return obj.__dict__
