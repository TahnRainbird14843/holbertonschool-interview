#!/usr/bin/python3

"""
This code solves the classic lockbox problem
"""


def canUnlockAll(boxes):
    """
    we solve it by opening each new box until
    we hit the most steps possible that would lead
    to opening all boxes if possible
    """
    keys = {0}
    new_keys = set()

    for _ in range(len(boxes)):
        for key in keys:
            if (key < len(boxes)):
                new_keys.update(boxes[key])
        keys.update(new_keys)

    return (len(set(keys)) == len(boxes))

