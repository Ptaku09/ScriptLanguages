import re


def is_line_valid(line):
    return re.search(r"^.* - - \[\d+/\w+/\d+:\d+:\d+:\d+ \S+] \".*\" \d{3} (\d+|-)$", line)


def get_address(line):
    return re.search(r"^\S+", line).group()


def get_date(line):
    return re.search(r"\[\d+/\w+/\d+:\d+:\d+:\d+ \S+]", line).group()[1:-1]  # [1:-1] removes the brackets


def get_request_method(line):
    method = re.search(r"(GET|POST|PUT|DELETE|HEAD|OPTIONS|CONNECT|TRACE)", line)

    if method:
        return method.group()

    return ""


def get_path(line):
    method_and_path = re.search(r"\".*\"", line).group()

    if "/" not in method_and_path:
        return ""

    return re.search(r"/(\S+)?", method_and_path).group()  # (\S+) matches any non-whitespace character


def get_protocol(line):
    protocol = re.search(r"HTTP/\d.\d", line)

    if protocol:
        return protocol.group()

    return ""


def get_response_status(line):
    fragment = re.search(r"\" \d{3} .*?$", line).group()  # get fragment from " to the end of the line, ex. " 200 6245

    return re.search(r"\d{3}", fragment).group()  # status code is the first 3 digits


def get_response_size(line):
    size = re.search(r"\d+$", line)

    if size:
        return size.group()

    return 0
