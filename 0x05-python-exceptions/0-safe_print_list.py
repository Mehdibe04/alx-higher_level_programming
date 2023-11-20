#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return 0
    cnt = 0
    try:
        for y in range(x):
            print("{}".format(my_list[y]), end="")
            cnt = cnt + 1
        print()
    except IndexError:
        print()
        pass
    return cnt
