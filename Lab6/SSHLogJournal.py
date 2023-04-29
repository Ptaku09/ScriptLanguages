import datetime
import ipaddress
import re

from SSHLogFactory import log_factory


class SSHLogJournal:
    def __init__(self):
        self.logs = []

    def append(self, log):
        log_obj = log_factory.create_log(log)
        self.logs.append(log_obj)

    def get_logs_by_ip(self, ip):
        if re.search(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip) is None:
            raise ValueError("Invalid IP address")

        ip = ipaddress.IPv4Address(ip)

        return [log for log in self.logs if log.ip == ip]

    def get_logs_by_date(self, date):
        if re.search(r'^\d{2}-\d{2}-\d{4}$', date) is None:
            raise ValueError("Invalid date")

        date = datetime.datetime.strptime(date, "%d-%m-%Y").date()

        return [log for log in self.logs if datetime.datetime.strptime(log.date, "%d-%m-%Y") == date]

    def __len__(self):
        return len(self.logs)

    def __iter__(self):
        return iter(self.logs)

    def __contains__(self, item):
        return item in self.logs
