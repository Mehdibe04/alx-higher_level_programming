#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_lst = []
    for y in range(list_length):
        try:
            res = my_list_1[y] / my_list_2[y]
        except (TypeError):
            print("wrong type")
            res = 0
        except (ZeroDivisionError):
            print("division by 0")
            res = 0
        except (IndexError):
            print("out of range")
            res = 0
        finally:
            n_lst.append(res)
    return n_lst