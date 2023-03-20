import datetime
import re

from my_utils import is_line_valid


def print_fridays():
    while True:
        try:
            line = input()

            if not is_line_valid(line):
                raise ValueError("Invalid line")

            date_fragment = re.search(r"\[.*?]", line).group()
            date = date_fragment[1:-1]
            day = datetime.datetime.strptime(date, "%d/%b/%Y:%H:%M:%S %z").weekday()

            if day == 4:
                print(line)

        except EOFError:
            break


if __name__ == '__main__':
    print_fridays()
