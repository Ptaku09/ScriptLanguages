import re
from enum import Enum
from typing import Match, Optional, List


def is_line_valid(line: str) -> Optional[Match[str]]:
    return re.search(
        r'\w{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2}\s\w+\ssshd\[\d+]:.*', line)


def get_date(line: str) -> str:
    match = re.search(r'\w{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2}', line)
    if match:
        return match.group(0)
    else:
        raise ValueError("Invalid date format")


def get_host_name(line: str) -> str:
    match = re.search(r'(?<=:\d{2} )\w+(?=\s)', line)
    if match:
        return match.group(0)
    else:
        raise ValueError("Invalid host name format")


def get_pid(line: str) -> str:
    match = re.search(r'(?<=\[)\d+(?=])', line)
    if match:
        return match.group(0)
    else:
        raise ValueError("Invalid PID format")


def get_message(line: str) -> str:
    match = re.search(r'(?<=]:\s).+', line)
    if match:
        return match.group(0)
    else:
        raise ValueError("Invalid message format")


def get_ipv4s_from_log(message: str) -> List[str]:
    return re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', message)


def get_user_from_log(message: str) -> Optional[str]:
    user_match = re.search(
        r'((?<=(user\s(?!request)(?!authentication)))|(?<=((?<!getaddrinfo)(?<!Thank you)\sfor\s(?!invalid)))|(?<=(\suser=)))\S+',
        message)

    if user_match:
        return user_match.group(0)
    else:
        return None


def get_port_from_log(message: str) -> Optional[str]:
    port_match = re.search(r'(?<=port\s)\d+', message)

    if port_match:
        return port_match.group(0)
    else:
        return None


class MessageType(Enum):
    FAILED_PASSWORD = 'Failed password'
    ACCEPTED_PASSWORD = 'Accepted password'
    ERROR = 'Error'
    OTHER = 'Other'


def get_message_type(message: str) -> MessageType:
    if re.search(r'^Failed password', message):
        return MessageType.FAILED_PASSWORD

    if re.search(r'^Accepted password', message):
        return MessageType.ACCEPTED_PASSWORD

    if re.search(r'^error:', message):
        return MessageType.ERROR

    return MessageType.OTHER
