#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list.copy()
    new_list.sort()
    res = 0
    a = 0
    for i in new_list:
        if i != a:
            res += i
            a = i
    return res
