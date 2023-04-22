import random

from lab_5_1 import read_ssh_logs, parse_ssh_logs
from lab_5_2 import get_user_from_log


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


if __name__ == '__main__':
    lines = read_ssh_logs('/Users/mateusz/Desktop/Studia/Semestr IV/[L] Języki skrytpowe/Lab5/test.log')
    parsed = parse_ssh_logs(lines)

    random_logs = get_random_sample_from_random_user_logs(parsed, 3)

    for lo in random_logs:
        print(lo)
