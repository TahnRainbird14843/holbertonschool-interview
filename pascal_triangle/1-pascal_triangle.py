#!/usr/bin/env python3

"""
custom function calculates the factorial of an integer n
"""
def factorial(n):
    out = 1
    while (n > 0):
        out *= n
        n -= 1

    return (out)

"""
custom function calculates i choose j (the number of ways to select i elements
from j element unordered)
"""
def choose(i, j):
    return (factorial(i) // (factorial(j) * factorial(i - j)))

"""
computes the first n rows of pascals triangle
"""
def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(choose(i, j))
        triangle.append(row)

    return (triangle)
