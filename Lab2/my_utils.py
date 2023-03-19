import re


def is_line_valid(line):
    return re.search(r"^.* - - \[\d+/\w+/\d+:\d+:\d+:\d+ .*] \".*\" \d{3} \d+|-", line)
