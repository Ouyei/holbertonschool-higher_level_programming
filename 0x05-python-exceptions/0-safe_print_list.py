#!/usr/bin/python3
# 0-safe_print_list.py
# Oscar Bedat <3961@holbertonschool.com>
def safe_print_list(my_list=[], x=0):
        ret = 0
        try:
            for element in my_list:
                if ret < x:
                    print('{}'.format(my_list[ret]), end='')
                    ret +=1
        except IndexError:
            pass
        finally:
            return ret
