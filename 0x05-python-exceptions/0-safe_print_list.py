#!/usr/bin/python3
# 0-safe_print_list.py
# Oscar Bedat <3961@holbertonschool.com>
def safe_print_list(my_list=[], x=0):
    items = 0
    for elements in range(x):
        try:
            print(my_list[elements]), end='')
            items += 1
    except IndexError:
        break
    print()
    return items
