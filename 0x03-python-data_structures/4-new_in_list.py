#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_listc = my_list.copy()
        my_listc[idx] = element
        return my_listc
    return my_list
