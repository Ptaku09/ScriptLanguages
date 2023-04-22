import re


def read_ssh_logs(log_file):
    with open(log_file, 'r') as f:
        logs = f.readlines()
    return logs


def parse_ssh_logs(logs):
    parsed_logs = []

    for log in logs:
        converted_line = line_to_dict(log)
        parsed_logs.append(converted_line)

    return parsed_logs


def line_to_dict(line):
    return {'date': get_date(line), 'host_name': get_host_name(line), 'app_component': get_app_component(line),
            'pid': get_pid(line), 'message': get_message(line)}


def get_date(line):
    return re.search(r'\w{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2}', line).group(0)


def get_host_name(line):
    return re.search(r'(?<=:\d{2} )\w+(?=\s)', line).group(0)


def get_app_component(line):
    return re.search(r'(?<=\s)\w+(?=\[)', line).group(0)


def get_pid(line):
    return re.search(r'(?<=\[)\d+(?=])', line).group(0)


def get_message(line):
    return re.search(r'(?<=]:\s).+', line).group(0)


if __name__ == '__main__':
    lines = read_ssh_logs('/Users/mateusz/Desktop/Studia/Semestr IV/[L] Języki skrytpowe/Lab5/test.log')
    parsed = parse_ssh_logs(lines)

    for li in parsed:
        print(li)
