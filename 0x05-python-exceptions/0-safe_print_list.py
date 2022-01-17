#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ret = 0
    try:
        for element in my_list:
            if ret < x:
                print('{}'.format(my_list[ret]), end='')
                ret +=1

        print()
    except IndexError:
        pass
    finally:
        return ret
