#!/usr/bin/python3

"""
Checks if data is a valid UTF8 encoding
"""


def validUTF8(data):
    """this function does the check"""
    i = 0
    for num in data:
        print([int(j) for j in list('{0:0b}'.format(num))])
    while i < len(data):
        bits = [int(j) for j in list('{0:0b}'.format(data[i]))]
        skip = -1
        for bit in bits:
            if (bit != 1):
                break
            skip += 1
        if skip <= 0:
            i += 1
        else:
            i += skip + 1
        if i > len(data):
            return False
    return True
