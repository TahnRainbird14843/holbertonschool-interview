#!/usr/bin/python3

"""
solves min operations
"""


def minOperations(n):
    """recursively gets minimum operations"""
    if (n <= 1):
        return 0
    curr_ops = 2
    while (n % curr_ops != 0):
        curr_ops += 1
    return (curr_ops + minOperations(n // curr_ops))
