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


def get_date(line):
    return re.search(r"\[\d+/\w+/\d+:", line).group()[1:-1]  # [1:-1] removes the unwanted characters


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


# Start the index.html file
eel.start("index.html", size=(800, 500))
