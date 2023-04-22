import random

from lab_5_1 import read_ssh_logs, parse_ssh_logs
from lab_5_2 import get_user_from_log, get_message_type, MessageType


def group_logs_by_user(logs):
    grouped_logs = {}

    for log in logs:
        user = get_user_from_log(log)

        if user:
            if user not in grouped_logs:
                grouped_logs[user] = []

            grouped_logs[user].append(log)

    return grouped_logs


def get_random_sample_from_random_user_logs(logs, n):
    grouped_logs = group_logs_by_user(logs)
    random_user = random.choice(list(grouped_logs.keys()))

    try:
        random_sample = random.sample(grouped_logs[random_user], n)
    except ValueError:
        print('Not enough logs for user: ' + random_user)
        random_sample = grouped_logs[random_user]

    return random_sample


def least_and_most_active_user(logs):
    grouped_logs = group_logs_by_user(logs)
    max_success_logins = 0
    min_success_logins = float('inf')
    max_users = []
    min_users = []

    for key, value in grouped_logs.items():
        user_success_logging = 0

        for log in value:
            message_type = get_message_type(log['message'])
            if message_type == MessageType.SUCCESSFUL_LOGGING.value:
                user_success_logging += 1

        if user_success_logging == max_success_logins:
            max_users.append(key)
        elif user_success_logging > max_success_logins:
            max_users.clear()
            max_users.append(key)
            max_success_logins = user_success_logging

        if user_success_logging == min_success_logins:
            min_users.append(key)
        elif user_success_logging < min_success_logins:
            min_users.clear()
            min_users.append(key)
            min_success_logins = user_success_logging

    print('Max success logins: ' + str(max_success_logins))
    print('Max success logins users: ' + str(max_users))
    print('------------------------')
    print('Min success logins: ' + str(min_success_logins))
    print('Min success logins users: ' + str(min_users))


if __name__ == '__main__':
    lines = read_ssh_logs('/Users/mateusz/Desktop/Studia/Semestr IV/[L] Języki skrytpowe/Lab5/SSH.log')
    parsed = parse_ssh_logs(lines)

    random_logs = get_random_sample_from_random_user_logs(parsed, 3)

    for lo in random_logs:
        print(lo)

    least_and_most_active_user(parsed)
