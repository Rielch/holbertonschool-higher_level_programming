#!/usr/bin/python3
a = 0
for x in range(122, 96, -1):
    if a == 1:
        x = x - 32
    print("{:c}".format(x), end='')
    if a == 0:
        a = 1
    else:
        a = 0
