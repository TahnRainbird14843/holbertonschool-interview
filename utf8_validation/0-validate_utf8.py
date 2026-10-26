#!/usr/bin/python3

def validUTF8(data):
    for num in data:
        if num >= 256:
            return False
    return True
