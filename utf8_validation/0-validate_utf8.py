#!/usr/bin/python3

"""
Checks if data is a valid UTF8 encoding
"""


def validUTF8(data):
    """this function does the check"""
    cont = 0
    for number in data:
        byte = number & 0xFF
        valid_byte_lookup = {
                byte >> 7 == 0b0: 0,
                byte >> 6 == 0b10: -1,
                byte >> 5 == 0b110: 1,
                byte >> 4 == 0b1110: 2,
                byte >> 3 == 0b11110: 3,
                byte >> 3 == 0b11111: None
                }[True]
        cont_add = valid_byte_lookup
        if (cont is None):
            return False
        if ((cont > 0 and cont_add >=0) or
                (cont == 0 and cont_add < 0)):
            return False
        cont += cont_add
    return (not bool(cont))
