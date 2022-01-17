#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    items = 0
    try:
        for elements in range(0, x):
            print("{}".format(my_list[elements]), end="")
            items += 1
    except IndexError:
        pass
    print()
    return items
