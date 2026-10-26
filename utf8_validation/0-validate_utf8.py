#!/usr/bin/python3

"""
Checks if data is a valid UTF8 encoding
"""


def validUTF8(data):
    """this function does the check"""
    for num in data:
        if num >= 256:
            return False
    return True
