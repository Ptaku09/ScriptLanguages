import re

from my_utils import is_line_valid


def print_200s():
    while True:
        try:
            line = input()

            if not is_line_valid(line):
                raise ValueError("Invalid line")
            elif re.search("\" 200 .*?$", line):
                print(line)

        except EOFError:
            break


if __name__ == '__main__':
    print_200s()
