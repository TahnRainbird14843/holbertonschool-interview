import re
import sys


def main():
    total_size = 0
    i = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            tokens = line.split()
            status = tokens[-2]
            size = tokens[-1]
            if not (status.isnumeric() and size.isnumeric()):
                raise Exception("Incorrect log format")
            total_size += int(size)
            status_codes[str(status)] += 1
            if (i % 10 == 0):
                print(f"File size: {total_size}")
                print(f"{status_codes}")
                i = 0
    except:
        pass
    finally:
        print(f"File size: {total_size}")
        print(f"{status_codes}")

    if __name__ == "__main__":
        main()