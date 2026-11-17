#!/usr/bin/python3

"""this is documented"""


def makeChange(coins, total):
    """do the thing"""
    found = []

    def nextCoin(used_coins, index):
        """iterably do the thing"""
        if sum(used_coins) == total:
            found.append(len(used_coins))

        for i, coin in enumerate(coins[index:]):
            if (sum(used_coins) + coin <= total):
                used_coins.append(coin)
                nextCoin(used_coins, index + i)
                del used_coins[-1]

    nextCoin([], 0)

    if found:
        return min(found)
    return -1

