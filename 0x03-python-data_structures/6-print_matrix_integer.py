#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for part in range(len(matrix)):
        for num in range(len(matrix[part])):
            print("{:d}".format(matrix[part][num]), end='')
            if num != len(matrix[part]) - 1:
                print(" ", end='')
        print("")
