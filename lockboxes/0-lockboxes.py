#!/usr/bin/python3

def canUnlockAll(boxes):
    keys = {0}
    new_keys = set()

    for _ in range(len(boxes)):
        for key in keys:
            new_keys.update(boxes[key])
        keys.update(new_keys)

    return (len(set(keys)) == len(boxes))

