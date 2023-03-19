import re

from my_utils import is_line_valid


def count_res_code_freq(code):
    counter = 0

    while True:
        try:
            line = input()

            if not is_line_valid(line):
                raise ValueError("Invalid line")
            elif re.search(f" {code} .*$", line):
                counter += 1

        except EOFError:
            break

    return counter
