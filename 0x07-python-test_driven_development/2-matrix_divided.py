#!/usr/bin/python3
"""Divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    The matrix can only contain integers or floats
    Every row of the matrix has to be the same size
    div has to be a number and can't be 0
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    a = 0
    if matrix[0]:
        a = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != a:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) is not float and type(element) is not int:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    
