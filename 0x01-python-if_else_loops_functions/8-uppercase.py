#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        if ord(str[x]) in range(97, 123):
            char = ord(str[x]) - 32
        else:
            char = ord(str[x])
        print("{:c}".format(char), end='')
    print("")
