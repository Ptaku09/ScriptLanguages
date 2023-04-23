import re
from enum import Enum

from lab_5_1 import read_ssh_logs, parse_ssh_logs


class MessageType(Enum):
    SUCCESSFUL_LOGGING = 'Successful logging'
    FAILED_LOGGING = 'Failed logging'
    CONNECTION_CLOSED = 'Connection closed'
    WRONG_PASSWORD = 'Wrong password'
    WRONG_USERNAME = 'Wrong username'
    BREAK_IN_ATTEMPT = 'Break-in attempt'
    OTHER = 'Other'


def get_ipv4s_from_log(line):
    message = line['message']
    return re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', message)


def get_user_from_log(line):
    message = line['message']
    user = re.search(
        r'((?<=(user\s(?!request)(?!authentication)))|(?<=((?<!getaddrinfo)(?<!Thank you)\sfor\s(?!invalid)))|(?<=(\suser=)))\S+',
        message)

    if user:
        return user.group(0)
    else:
        return None


def get_message_type(message):
    if re.search(r'^Accepted password', message):
        return MessageType.SUCCESSFUL_LOGGING.value

    if re.search(r'Connection closed|session closed|Received disconnect|Disconnecting:|Connection reset', message):
        return MessageType.CONNECTION_CLOSED.value

    if re.search(r'authentication failure;', message):
        return MessageType.FAILED_LOGGING.value

    if re.search(r'^Failed password', message):
        return MessageType.WRONG_PASSWORD.value

    if re.search(r'(^Invalid user|: invalid user)', message):
        return MessageType.WRONG_USERNAME.value

    if re.search(r'BREAK-IN ATTEMPT!$', message):
        return MessageType.BREAK_IN_ATTEMPT.value

    return MessageType.OTHER.value


if __name__ == '__main__':
    lines = read_ssh_logs('/Users/mateusz/Desktop/Studia/Semestr IV/[L] Języki skrytpowe/Lab5/test.log')
    parsed = parse_ssh_logs(lines)

    for li in parsed:
        print("ipv4s:", '------', get_ipv4s_from_log(li))
        print("user", '------', get_user_from_log(li))
        print(get_message_type(li['message']), '------', li['message'])
        print()
