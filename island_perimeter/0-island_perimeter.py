#!/usr/bin/python3

"""get the island perimeter"""


def count_border(grid, pos):
    """count the number of borders around a particular square"""
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
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
    land = [[i, j] for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1]
    border = 0
    for pos in land:
        border += count_border(grid, pos)
    return border
