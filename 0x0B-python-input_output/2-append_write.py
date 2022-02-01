#!/usr/bin/python3
# 2-append_write.py
# Oscar Bedat <3961@holbertonschool.com>
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """append_write appends a string at the end of a text file (UTF8)
    Args:
        filename (str): Defaults to "".
        text (str): text to add. Defaults to "".
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
