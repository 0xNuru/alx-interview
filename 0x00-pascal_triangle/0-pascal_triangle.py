#!/usr/bin/env python3
import math


def pascal_triangle(n):
    """
    a function that returns a list representing
    the Pascal’s triangle of n:
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(math.comb(i, j))
        triangle.append(row)

    return triangle
