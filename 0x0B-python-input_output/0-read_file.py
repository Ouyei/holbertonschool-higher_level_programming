#!/usr/bin/python3
# 0-read_file.py
# Oscar Bedat <3961@holbertonschool.com>


def read_file(filename=""):
    """read_file reads a text file (UTF8) and prints it to stdout
    Args:
        filename (str): content of the file. Defaults to "".
    """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
