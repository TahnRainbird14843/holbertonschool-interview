import re
import sys


def main():
    total_size = 0
    i = 0
    log_pattern = r'(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S*)" (\d{3}) (\d+)'
    status_codes = {"200": 0, "301": 0, "400": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            parsed = re.match(log_pattern, line)
            status = parsed.group(8)
            size = parsed.group(9)
            total_size += size
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