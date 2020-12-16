#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            a = 0
        else:
            a = tuple_a[0]
        c = 0
    else:
        a = tuple_a[0]
        c = tuple_a[1]
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            b = 0
        else:
            b = tuple_b[0]
        d = 0
    else:
        b = tuple_b[0]
        d = tuple_b[1]
    newtuple = a + b, c + d
    return newtuple
