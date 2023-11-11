#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniq_lst = []
    for i in my_list:
        if i not in uniq_lst:
            uniq_lst.append(i)
    for i in uniq_lst:
        sum += i
    return (sum)
