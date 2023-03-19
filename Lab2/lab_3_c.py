import re

from my_utils import is_line_valid, get_path


def print_path_and_max_size():
    line, max_size = find_max_size()
    path = get_path(line)
    print(f"{path} {max_size}")


def find_max_size():
    max_size = 0
    line_with_max_size = ""

    while True:
        try:
            line = input()

            if not is_line_valid(line):
                raise ValueError("Invalid line")
            elif re.search(r" \d+$", line):
                size = int(line.split()[-1])

                if size > max_size:
                    max_size = size
                    line_with_max_size = line

        except EOFError:
            break

    return line_with_max_size, max_size


if __name__ == '__main__':
    print_path_and_max_size()
