#!/usr/bin/python3
def search_replace(my_list, search, replace):
    Nwlist = my_list.copy()
    x = 0
    for i in my_list:
        if i is search:
            Nwlist[x] = replace
        x += 1
    return (Nwlist)
