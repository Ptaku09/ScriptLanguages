import re
from enum import Enum


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


def get_user_from_log(message):
    user = re.search(
        r'((?<=(user\s(?!request)(?!authentication)))|(?<=((?<!getaddrinfo)(?<!Thank you)\sfor\s(?!invalid)))|(?<=(\suser=)))\S+',
        message)

    if user:
        return user.group(0)
    else:
        return None


def get_port_from_log(message):
    port = re.search(r'(?<=port\s)\d+', message)

    if port:
        return port.group(0)
    else:
        return None


class MessageType(Enum):
    FAILED_PASSWORD = 'Failed password'
    ACCEPTED_PASSWORD = 'Accepted password'
    ERROR = 'Error'
    OTHER = 'Other'


def get_message_type(line):
    message = get_message(line)
    
    if re.search(r'^Failed password', message):
        return MessageType.FAILED_PASSWORD

    if re.search(r'^Accepted password', message):
        return MessageType.ACCEPTED_PASSWORD

    if re.search(r'^error:', message):
        return MessageType.ERROR

    return MessageType.OTHER
