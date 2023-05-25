import re
from enum import Enum
from typing import Match, Optional, List


def is_line_valid(line: str) -> Optional[Match[str]]:
    return re.search(
        r'\w{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2}\s\w+\ssshd\[\d+]:.*', line)


def get_date(line: str) -> str:
    return re.search(r'\w{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2}', line).group(0)


def get_host_name(line: str) -> str:
    return re.search(r'(?<=:\d{2} )\w+(?=\s)', line).group(0)


def get_pid(line: str) -> str:
    return re.search(r'(?<=\[)\d+(?=])', line).group(0)


def get_message(line: str) -> str:
    return re.search(r'(?<=]:\s).+', line).group(0)


def get_ipv4s_from_log(message: str) -> List[str]:
    return re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', message)


def get_user_from_log(message: str) -> Optional[str]:
    user: Match[str] = re.search(
        r'((?<=(user\s(?!request)(?!authentication)))|(?<=((?<!getaddrinfo)(?<!Thank you)\sfor\s(?!invalid)))|(?<=(\suser=)))\S+',
        message)

    if user:
        return user.group(0)
    else:
        return None


def get_port_from_log(message: str) -> Optional[str]:
    port: Match[str] = re.search(r'(?<=port\s)\d+', message)

    if port:
        return port.group(0)
    else:
        return None


class MessageType(Enum):
    FAILED_PASSWORD: str = 'Failed password'
    ACCEPTED_PASSWORD: str = 'Accepted password'
    ERROR: str = 'Error'
    OTHER: str = 'Other'


def get_message_type(message: str) -> MessageType:
    if re.search(r'^Failed password', message):
        return MessageType.FAILED_PASSWORD

    if re.search(r'^Accepted password', message):
        return MessageType.ACCEPTED_PASSWORD

    if re.search(r'^error:', message):
        return MessageType.ERROR

    return MessageType.OTHER
