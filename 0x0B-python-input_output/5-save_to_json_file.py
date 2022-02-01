#!/usr/bin/python3
# 5-save_to_json_file.py
# Oscar Bedat <3961@holbertonschool.com>
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file writes an object 2 a text file
    Args:
        my_obj (obj): any object for example list, dict
        filename: file name
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
