#!/usr/bin/python3
"""Returns a list of lists of integers representing the Pascal's triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's triangle
    n represents the size of the triangle
    """
    new_triangle = []
    if n <= 0:
        return new_triangle
    new_triangle.append([1])
    for i in range(1, n):
        new_triangle.append([])
        for a in range(i + 1):
            if a == 0 or a == i:
                new_triangle[i].append(1)
            else:
                new_triangle[i].append(new_triangle[i - 1][a] + new_triangle[i - 1][a - 1])
    return new_triangle
