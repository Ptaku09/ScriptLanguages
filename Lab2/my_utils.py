import re


def is_line_valid(line):
    return re.search(r"^.* - - \[\d+/\w+/\d+:\d+:\d+:\d+ .*] \".*\" \d{3} \d+|-", line)


def get_path(line):
    method_and_path = re.search(r"\".*\"", line).group()

    if "/" not in method_and_path:
        return ""

    return re.search(r"/(\S+)?", method_and_path).group()  # (\S+) matches any non-whitespace character
