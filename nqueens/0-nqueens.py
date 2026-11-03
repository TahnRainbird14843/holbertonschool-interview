#!/usr/bin/python3

"""
this solves the nqueens problem
"""

import sys


def is_safe(board, x, y, n):
    for i in range(n):
        if board[x][i] == "Q":
            return False

    for i in range(n):
        if board[i][y] == "Q":
            return False

    for i in range(-n, n):
        if (0 <= x + i < n and 0 <= y + i < n and board[x + i][y + i] == "Q"):
            return False

    for i in range(-n, n):
        if (0 <= x + i < n and 0 <= y - i < n and board[x + i][y - i] == "Q"):
            return False

    return True


def display_board(board):
    for row in board:
        print(row)
    print()


def nqueens(n):
    board = [["." for i in range(n)] for j in range(n)]
    result = []

    def attempt_place(board, col):
        if col == n:
            result.append([[i, j] for i in range(n)
                        for j in range(n) if board[i][j] == "Q"])
            return

        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = "Q"
                attempt_place(board, col + 1)
                board[row][col] = "."

    attempt_place(board, 0)
    for solution in result:
        print(solution)


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: nqueens N")
    elif (not sys.argv[1].isnumeric()):
        print("N must be a number")
    elif (int(sys.argv[1]) < 4):
        print("N must be at least 4")
    else:
        nqueens(int(sys.argv[1]))
