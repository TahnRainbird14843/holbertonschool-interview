#!/usr/bin/python3
 
import numpy as np

"""get the island perimeter"""


def count_border(grid, pos):
    """count the number of borders around a particular square"""
    directions = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]])
    border = 0
    for dir in directions:
        check = pos + dir
        try:
            if grid[check[0]][check[1]] == 0:
                border += 1
        except BaseException:
            pass
    return border


def island_perimeter(grid):
    """find the entire island perimeter"""
    grid = np.array(grid)
    land = np.array(np.where(grid == 1)).transpose()
    border = 0
    for pos in land:
        border += count_border(grid, pos)
    return border
