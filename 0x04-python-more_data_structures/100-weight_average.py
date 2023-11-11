#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    w = 0
    avrg = []
    for tuple in my_list:
        avrg.append(tuple[1])
        w += tuple[0] * tuple[1]
    return w / sum(avrg)
