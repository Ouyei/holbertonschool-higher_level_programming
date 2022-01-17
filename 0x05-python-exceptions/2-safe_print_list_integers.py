#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    items = 0
    for elements in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            items += 1
            except (ValueError, TypeError):
                continue
            print()
            return items
