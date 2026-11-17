#!/usr/bin/python3

"""this is documented"""

from math import gcd


def makeChange(coins, total):
    """do the thing"""
    if (total <= 0):
        return 0
    elif (len(coins) < 1):
        return -1
    
    coins.sort(reverse=True)

    if (len(coins) == 1):
        if (total % coins[0] == 0):
            return total // coins[0]
        return -1

    for i in range(total // coins[0], total // coins[0] - ((coins[0] * coins[1]) // gcd(coins[0], coins[1]) // coins[0]), -1):
        test_subset = makeChange(coins[1: ], total - i * coins[0])
        if (test_subset != -1):
            return test_subset + i

    return -1

