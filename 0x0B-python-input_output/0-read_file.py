#!/usr/bin/python3
# 0-read_file.py
# Oscar Bedat <3961@holbertonschool.com>


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(f.read(), end="")
