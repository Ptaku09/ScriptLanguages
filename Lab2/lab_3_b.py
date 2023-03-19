import re

from my_utils import is_line_valid


def print_sent_gigabytes():
    sent_bytes = sum_sent_bytes()
    sent_gigabytes = bytes_to_gigabytes(sent_bytes)
    print(f"{sent_gigabytes}GB")


def sum_sent_bytes():
    total_bytes = 0

    while True:
        try:
            line = input()

            if not is_line_valid(line):
                raise ValueError("Invalid line")
            elif re.search(r" \d+$", line):
                total_bytes += int(line.split()[-1])

        except EOFError:
            break

    return total_bytes


def bytes_to_gigabytes(b):
    return round(b * (10 ** -9), 2)


if __name__ == '__main__':
    print_sent_gigabytes()
