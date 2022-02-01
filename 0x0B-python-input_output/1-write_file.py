#!/usr/bin/python3
# 1-write_file.py
# Oscar Bedat <3961@holbertonschool.com>


def write_file(filename="", text=""):
    """write_file writes a string 2 a text file (UTF8)

    Args:
        filename (str): Defaults to "".
        text (str): text to add. Defaults to"".
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
