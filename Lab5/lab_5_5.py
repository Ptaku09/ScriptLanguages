import argparse

from lab_5_1 import read_ssh_logs, line_to_dict
from lab_5_2 import get_ipv4s_from_log, get_user_from_log, get_message_type
from lab_5_3 import get_logger
from lab_5_4 import get_random_sample_from_random_user_logs, get_avg_session_time_and_stddev_per_user, \
    get_avg_session_time_and_stddev, least_and_most_active_users

parser = argparse.ArgumentParser(description='Deal with some logs')

parser.add_argument('path', type=str, help='Path to log file')
parser.add_argument('-l', '--level', type=str, choices=['d', 'i', 'w', 'e', 'c'], default='i',
                    help='Logging level, d - DEBUG, i - INFO(default), w - WARNING, e - ERROR, c - CRITICAL')

subparsers = parser.add_subparsers(help='Subcommand help', dest='sub')

subparsers.add_parser('parse', help='Print parsed logs(converted to dict) (ex_2_a / ex_1_b)')
subparsers.add_parser('ipv4', help='Get all ipv4 addresses from log message (ex_2_b)')
subparsers.add_parser('user', help='Get user from log message (ex_2_c)')
subparsers.add_parser('type', help='Get message type from log message (ex_2_d)')

subparser_random = subparsers.add_parser('random_logs', help='Get random logs from random user (ex_4_a)')
subparser_random.add_argument('n', type=int, help='Number of logs to get')

subparser_connection = subparsers.add_parser('connection', help='Get connection time statistics (ex_4_b_i)')
subparser_connection.add_argument('-u', '--user', action='store_true',
                                  help='Get statistics for each user (ex_4_b_ii)')

subparsers.add_parser('activity', help='Get least and most active users (ex_4_c)')

args = parser.parse_args()

path = args.path
level = args.level
sub = args.sub

logger = get_logger(level)
logs = read_ssh_logs(path)

parsed_logs = []

for log in logs:
    # logger(log)
    parsed = line_to_dict(log)
    parsed_logs.append(parsed)

    if sub == 'parse':
        print(parsed)
    elif sub == 'ipv4':
        print("ipv4s: ", get_ipv4s_from_log(parsed))
    elif sub == 'user':
        print('User: ', get_user_from_log(parsed))
    elif sub == 'type':
        print('Message type: ', get_message_type(parsed['message']))

if sub == 'random_logs':
    n = args.n
    sample = get_random_sample_from_random_user_logs(parsed_logs, n)

    for sam in sample:
        print(sam)
elif sub == 'connection':
    if args.user:
        for user, (avg, stddev) in get_avg_session_time_and_stddev_per_user(parsed_logs).items():
            print(f'{user:15s} - avg: {avg:6.2f},\tstddev: {stddev:6.2f}')
    else:
        avg, stddev = get_avg_session_time_and_stddev(parsed_logs)
        print(f'avg: {avg:.2f},\tstddev: {stddev:.2f}')
elif sub == 'activity':
    least_and_most_active_users(parsed_logs)
