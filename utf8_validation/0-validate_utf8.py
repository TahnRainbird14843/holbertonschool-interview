#!/usr/bin/python3

"""
Checks if data is a valid UTF8 encoding
"""


def validUTF8(data):
    """this function does the check"""
    i = 0
    while i < len(data):
        bits = [int(j) for j in list('{0:0b}'.format(data[i]))]
        skip = bits[bits.index(1) + 1: bits.index(0)].count(1)
        i += skip + 1
        if i > len(data) or skip > 3:
            return False
    return True

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
