import typer

from lab_5_1 import read_ssh_logs, line_to_dict
from lab_5_1roz import detect_brute_force
from lab_5_2 import get_ipv4s_from_log, get_user_from_log, get_message_type
from lab_5_3 import get_logger
from lab_5_4 import get_random_sample_from_random_user_logs, get_avg_session_time_and_stddev_per_user, \
    get_avg_session_time_and_stddev, least_and_most_active_users

app = typer.Typer()


@app.command()
def parse(path: str, level: str = typer.Option('i', '-l', '--level',
                                               help='Logging level, d - DEBUG, i - INFO(default), w - WARNING, e - ERROR, c - CRITICAL',
                                               show_default=True, case_sensitive=False)):
    logger = get_logger(level)
    logs = read_ssh_logs(path)

    for log in logs:
        # logger(log)
        parsed = line_to_dict(log)
        print(parsed)


@app.command()
def ipv4(path: str, level: str = typer.Option('i', '-l', '--level',
                                              help='Logging level, d - DEBUG, i - INFO(default), w - WARNING, e - ERROR, c - CRITICAL',
                                              show_default=True, case_sensitive=False)):
    logger = get_logger(level)
    logs = read_ssh_logs(path)

    for log in logs:
        # logger(log)
        parsed = line_to_dict(log)
        print("ipv4s: ", get_ipv4s_from_log(parsed))


@app.command()
def user(path: str, level: str = typer.Option('i', '-l', '--level',
                                              help='Logging level, d - DEBUG, i - INFO(default), w - WARNING, e - ERROR, c - CRITICAL',
                                              show_default=True, case_sensitive=False)):
    logger = get_logger(level)
    logs = read_ssh_logs(path)

    for log in logs:
        # logger(log)
        parsed = line_to_dict(log)
        print('User: ', get_user_from_log(parsed))


@app.command()
def type(path: str, level: str = typer.Option('i', '-l', '--level',
                                              help='Logging level, d - DEBUG, i - INFO(default), w - WARNING, e - ERROR, c - CRITICAL',
                                              show_default=True, case_sensitive=False)):
    logger = get_logger(level)
    logs = read_ssh_logs(path)

    for log in logs:
        # logger(log)
        parsed = line_to_dict(log)
        print('Message type: ', get_message_type(parsed['message']))


@app.command()
def random_logs(path: str, n: int, level: str = typer.Option('i', '-l', '--level',
                                                             help='Logging level, d - DEBUG, i - INFO(default), w - WARNING, e - ERROR, c - CRITICAL',
                                                             show_default=True, case_sensitive=False)):
    logger = get_logger(level)
    logs = read_ssh_logs(path)
    parsed_logs = []

    for log in logs:
        # logger(log)
        parsed_logs.append(line_to_dict(log))

    sample = get_random_sample_from_random_user_logs(parsed_logs, n)

    for sam in sample:
        print(sam)


@app.command()
def connection(path: str, level: str = typer.Option('i', '-l', '--level',
                                                    help='Logging level, d - DEBUG, i - INFO(default), w - WARNING, e - ERROR, c - CRITICAL',
                                                    show_default=True, case_sensitive=False), user: bool = False):
    logger = get_logger(level)
    logs = read_ssh_logs(path)
    parsed_logs = []

    for log in logs:
        # logger(log)
        parsed_logs.append(line_to_dict(log))

    if user:
        for usr, (avg, stddev) in get_avg_session_time_and_stddev_per_user(parsed_logs).items():
            print(f'{usr:15s} - avg: {avg:6.2f},\tstddev: {stddev:6.2f}')
    else:
        avg, stddev = get_avg_session_time_and_stddev(parsed_logs)
        print(f'avg: {avg:.2f},\tstddev: {stddev:.2f}')


@app.command()
def activity(path: str, level: str = typer.Option('i', '-l', '--level',
                                                  help='Logging level, d - DEBUG, i - INFO(default), w - WARNING, e - ERROR, c - CRITICAL',
                                                  show_default=True, case_sensitive=False)):
    logger = get_logger(level)
    logs = read_ssh_logs(path)
    parsed_logs = []

    for log in logs:
        # logger(log)
        parsed_logs.append(line_to_dict(log))

    least_and_most_active_users(parsed_logs)


@app.command()
def brute_force(path: str, interval: int, level: str = typer.Option('i', '-l', '--level',
                                                                    help='Logging level, d - DEBUG, i - INFO(default), w - WARNING, e - ERROR, c - CRITICAL',
                                                                    show_default=True, case_sensitive=False),
                user: bool = False):
    logger = get_logger(level)
    logs = read_ssh_logs(path)
    parsed_logs = []

    for log in logs:
        # logger(log)
        parsed_logs.append(line_to_dict(log))

    if user:
        detect_brute_force(parsed_logs, interval, True)
    else:
        detect_brute_force(parsed_logs, interval)


if __name__ == "__main__":
    app()
