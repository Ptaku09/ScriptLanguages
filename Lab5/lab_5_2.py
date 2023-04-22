import re

from lab_5_1 import read_ssh_logs, parse_ssh_logs


def get_ipv4s_from_log(line):
    message = line['message']
    return re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', message)


def get_user_from_log(line):
    message = line['message']
    user = re.search(r'((?<=(user\s(?!request)))|(?<=((?<!getaddrinfo)\sfor\s(?!invalid)))|(?<=(\suser=)))\S+', message)

    if user:
        return user.group(0)
    else:
        return None


def get_message_type(message):
    if re.search(r'^Accepted password', message):
        return 'Successful logging'

    if re.search(r'authentication failure', message):
        return 'Failed logging'

    if re.search(r'^Connection closed', message):
        return 'Connection closed'

    if re.search(r'^Failed password', message):
        return 'Wrong password'

    if re.search(r'(^Invalid user|: invalid user)', message):
        return 'Wrong username'

    if re.search(r'ATTEMPT!$', message):
        return 'Break-in attempt'

    return 'Other'


if __name__ == '__main__':
    lines = read_ssh_logs('/Users/mateusz/Desktop/Studia/Semestr IV/[L] Języki skrytpowe/Lab5/test.log')
    parsed = parse_ssh_logs(lines)

    for li in parsed:
        print(get_message_type(li['message']), '------', li['message'])
