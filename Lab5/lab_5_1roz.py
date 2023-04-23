import datetime

from lab_5_1 import read_ssh_logs, parse_ssh_logs
from lab_5_2 import get_message_type, MessageType, get_ipv4s_from_log, get_user_from_log


def detect_brute_force(logs, max_interval, single_user=False):
    if single_user:
        failed_logins = get_failed_logins_by_ip_per_user(logs)
        brute_forces = {}

        for user, failed in failed_logins.items():
            for ip, fail in failed.items():
                if is_brute_force(fail, max_interval):
                    if user not in brute_forces:
                        brute_forces[user] = [(fail[0]["date"], ip, len(fail))]
                    else:
                        brute_forces[user].append((fail[0]["date"], ip, len(fail)))

        print_user_results(brute_forces)
    else:
        failed_logins = get_failed_logins_by_ip(logs)
        brute_forces = []

        for ip, failed_logins in failed_logins.items():
            if is_brute_force(failed_logins, max_interval):
                brute_forces.append((failed_logins[0]["date"], ip, len(failed_logins)))

        print_results(brute_forces)


def get_failed_logins_by_ip_per_user(logs):
    ip_failed_logins = {}

    for log in logs:
        message_type = get_message_type(log['message'])

        if message_type == MessageType.WRONG_PASSWORD.value:
            ip = get_ipv4s_from_log(log)[0]
            user = get_user_from_log(log)

            if user:
                if user not in ip_failed_logins:
                    ip_failed_logins[user] = {}

                if ip in ip_failed_logins[user]:
                    ip_failed_logins[user][ip].append(log)
                else:
                    ip_failed_logins[user][ip] = [log]

    return ip_failed_logins


def get_failed_logins_by_ip(logs):
    ip_failed_logins = {}

    for log in logs:
        message_type = get_message_type(log['message'])

        if message_type == MessageType.WRONG_PASSWORD.value:
            ip = get_ipv4s_from_log(log)[0]

            if ip in ip_failed_logins:
                ip_failed_logins[ip].append(log)
            else:
                ip_failed_logins[ip] = [log]

    return ip_failed_logins


def is_brute_force(failed_logins, interval):
    if len(failed_logins) > 1:
        last_failed = datetime.datetime.strptime(failed_logins[0]['date'], '%b %d %H:%M:%S')

        for failed in failed_logins[1:]:
            login_time = datetime.datetime.strptime(failed['date'], '%b %d %H:%M:%S')

            if (login_time - last_failed).total_seconds() <= interval:
                return True

            last_failed = login_time

    return False


def print_user_results(res):
    for user, failed_logins in res.items():
        print(f'User: {user}')
        print(f'{"Date":17s} {"IP":17s} {"Failed logins"}')
        print('-' * 50)

        for date, ip, tries in failed_logins:
            print(f'{date:17s} {ip:17s} {tries}')

        print()


def print_results(res):
    print(f'{"Date":17s} {"IP":17s} {"Failed logins"}')
    print('-' * 50)

    for date, ip, failed_logins in res:
        print(f'{date:17s} {ip:17s} {failed_logins}')


if __name__ == '__main__':
    lines = read_ssh_logs('/Users/mateusz/Desktop/Studia/Semestr IV/[L] Języki skrytpowe/Lab5/SSH.log')
    parsed = parse_ssh_logs(lines)

    detect_brute_force(parsed, 0.5)
