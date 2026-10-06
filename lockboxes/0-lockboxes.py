#!/usr/bin/python3

"""
This code solves the classic lockbox problem
"""


def canUnlockAll(boxes):
    keys = {0}

    for _ in range(len(boxes)):
        new_keys = set()
        for key in keys:
            new_keys.update([k for k in boxes[key] if k < len(boxes)])
            boxes[key] = []
        keys.update(list(new_keys))

    for box in boxes:
        if box:
            return False
    return True
