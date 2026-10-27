#!/usr/bin/python3

"""
Checks if data is a valid UTF8 encoding
"""


def validUTF8(data):
    """this function does the check"""
    i = 0
    while i < len(data):
        bits = [int(j) for j in list('{0:08b}'.format(data[i] % 256))]
        if bits[0] == 1:
            skip = bits[1: bits.index(0)].count(1)
        else:
            skip = 0
        if skip > 3:
            return False
        while skip > 0:
            i += 1
            bits = [int(j) for j in list('{0:08b}'.format(data[i] % 256))]
            if not (bits[0] == 1 and bits[1] == 0):
                return False
            skip -= 1
        i += 1
        if i > len(data):
            return False
    return True
