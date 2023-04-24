import re


def is_line_valid(line):
    return re.search(
        r'\w{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2}\s\w+\ssshd\[\d+]:.*', line)


def get_date(line):
    return re.search(r'\w{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2}', line).group(0)


def get_host_name(line):
    return re.search(r'(?<=:\d{2} )\w+(?=\s)', line).group(0)


def get_pid(line):
    return re.search(r'(?<=\[)\d+(?=])', line).group(0)


def get_message(line):
    return re.search(r'(?<=]:\s).+', line).group(0)


def get_ipv4s_from_log(message):
    return re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', message)
