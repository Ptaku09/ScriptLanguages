import re
from datetime import datetime, timedelta

import eel

eel.init("web")


@eel.expose
def read_logs(path):
    try:
        with open(path, "r") as f:
            return {"status": "success", "logs": f.readlines()}
    except FileNotFoundError:
        return {"status": "error", "logs": []}


@eel.expose
def filter_logs_by_date(logs, start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    return [log for log in logs if
            start_date <= datetime.strptime(get_date(log), "%d/%b/%Y") <= end_date + timedelta(days=1)]


@eel.expose
def get_js_date(line):
    date_string = get_date(line)
    return parse_date_to_js_format(date_string)


def parse_date_to_js_format(date):
    months = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    }

    day, month, year = date.split('/')
    month = months[month]

    return f"{month}.{int(day) + 1}.{year}"


@eel.expose
def get_log_details(line):
    if is_line_valid(line):
        return {
            "host": get_remote_host(line),
            "date": get_date(line),
            "time": get_time(line),
            "timezone": get_timezone(line),
            "status_code": get_status_code(line),
            "method": get_method(line),
            "resource": get_resource(line),
            "size": get_size(line) + " bytes"
        }
    else:
        return {
            "host": "Line is not valid",
            "date": "-",
            "time": "-",
            "timezone": "-",
            "status_code": "-",
            "method": "-",
            "resource": "-",
            "size": "-"
        }


def is_line_valid(line):
    return re.search(r"^.* - - \[\d+/\w+/\d+:\d+:\d+:\d+ \S+] \".*\" \d{3} (\d+|-)$", line)


def get_remote_host(line):
    return re.search(r"^\S+", line).group()


def get_date(line):
    return re.search(r"\[\d+/\w+/\d+:", line).group()[1:-1]  # [1:-1] removes the unwanted characters


def get_time(line):
    return re.search(r"(?<=:)\d+:\d+:\d+", line).group()


def get_timezone(line):
    return re.search(r"(\\+|-)\d{4}", line).group()


def get_status_code(line):
    fragment = re.search(r"\" \d{3} .*?$", line).group()  # get fragment from " to the end of the line, ex. " 200 6245

    return re.search(r"\d{3}", fragment).group()  # status code is the first 3 digits


def get_method(line):
    method = re.search(r"(GET|POST|PUT|DELETE|HEAD|OPTIONS|CONNECT|TRACE)", line)

    if method:
        return method.group()

    return ""


def get_resource(line):
    method_and_path = re.search(r"\".*\"", line).group()

    if "/" not in method_and_path:
        return ""

    return re.search(r"/(\S+)?", method_and_path).group()  # (\S+) matches any non-whitespace character


def get_size(line):
    size = re.search(r"\d+$", line)

    if size:
        return size.group()

    return '0'


# Start the index.html file
eel.start("index.html", size=(800, 500))
