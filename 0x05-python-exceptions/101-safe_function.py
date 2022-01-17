#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except IndexError as error:
        print("Exception: {}".format(e), file=stderr)
        return None
