import re

from my_utils import is_line_valid


def print_22_6():
    while True:
        try:
            line = input()

            if not is_line_valid(line):
                raise ValueError("Invalid line")

            date_fragment = re.search(r"\[.*?]", line).group(0)
            time = date_fragment.split(" ")[0][-8:]

            if int(time[0:2]) >= 22 or int(time[0:2]) < 6:
                print(line)

        except EOFError:
            break


if __name__ == '__main__':
    print_22_6()
