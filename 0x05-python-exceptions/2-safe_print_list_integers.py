#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    a = x
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            a -= 1
    print("", end="\n")
    return a
