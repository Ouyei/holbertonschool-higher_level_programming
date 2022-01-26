#!/usr/bin/python3
# 5-text_indentation.py
# Oscar Bedat <3961@holbertonschool.com>
"""
This module prints a text with a 2 new lines after each of
these characters: `.`, `?`, `:`
Example:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
    $
    Quonam modo?$
    $
    Utrum igitur tibi litteram videor an totas paginas commovere?$
    $
    Non autem hoc:$
    $
    * text must be a string
    * There should be no space at the beginning or
    at the end of each printed line
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
