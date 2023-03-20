import re

from my_utils import is_line_valid


def print_pl_requests():
    while True:
        try:
            line = input()

            if not is_line_valid(line):
                raise ValueError("Invalid line")

            req_url = re.search(r"^.* - -", line).group()[:-4]

            if re.search(r".pl$", req_url):
                print(line)

        except EOFError:
            break


if __name__ == '__main__':
    print_pl_requests()
