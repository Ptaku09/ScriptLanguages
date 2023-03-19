import re

from my_utils import is_line_valid, get_path


def print_ratio_of_graphics():
    prop = calc_ratio_of_graphics()
    print(f"The ratio of graphic downloads: {prop:.2f}")


def calc_ratio_of_graphics():
    graphics = 0
    rest = 0

    while True:
        try:
            line = input()

            if not is_line_valid(line):
                raise ValueError("Invalid line")

            path = get_path(line)

            if re.search(r"\.(gif|jpg|jpeg|xbm)$", path):
                graphics += 1
            else:
                rest += 1

        except EOFError:
            break

    return graphics / (graphics + rest)


if __name__ == '__main__':
    print_ratio_of_graphics()
