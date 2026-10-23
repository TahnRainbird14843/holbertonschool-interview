#!/usr/bin/python3

"""
log parsing
"""

import sys


def print_stats(total_size, status_codes):
    """this prints the relevant stats"""
    print(f"File size: {total_size}")
    for _, (key, value) in enumerate(status_codes.items()):
        if (value != 0):
            print(f"{key}: {value}")


def main():
    """this is the main loop"""
    total_size = 0
    i = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            line = line.strip()
            tokens = line.split()
            status = tokens[-2]
            size = tokens[-1]
            if (status.isnumeric() and size.isnumeric()):
                total_size += int(size)
                status_codes[str(status)] += 1
            i += 1
            if (i % 10 == 0 and i != 0):
                print_stats(total_size, status_codes)
                i = 0
    except:
        pass
    finally:
        print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
