#!/usr/bin/env python3

def pascal_triangle(n):
    if (n <= 0):
        return ([])
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(i - 1):
            row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        row.append(1)
        triangle.append(row)

    return (triangle)
