#!/usr/bin/python3
# 6-load_from_json_file.py
# Oscar Bedat <3961@holbertonschool.com>
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """ def load_from_json_file(filename): creates an Object from a JSON file
    Args:
        my_obj (obj): any object for example list, dict
        filename: file name
    """
    with open(filename) as f:
        return json.load(f)
