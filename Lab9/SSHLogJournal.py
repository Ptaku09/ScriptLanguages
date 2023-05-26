import ipaddress
import re
from typing import Iterator, List

from SSHLogFactory import log_factory, Log


class SSHLogJournal:
    def __init__(self) -> None:
        self.logs: List[Log] = []

    def append(self, log_entry: str) -> None:
        log_obj: Log = log_factory.create_log(log_entry)
        self.logs.append(log_obj)

    def get_logs_by_ip(self, ip_address: str) -> List[Log]:
        if re.search(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip_address) is None:
            raise ValueError("Invalid IP address")

        ip_obj: ipaddress.IPv4Address = ipaddress.IPv4Address(ip_address)

        return [log for log in self.logs if log.ip == ip_obj]

    def __len__(self) -> int:
        return len(self.logs)

    def __iter__(self) -> Iterator[Log]:
        return iter(self.logs)

    def __contains__(self, item: str) -> bool:
        return item in self.logs


if __name__ == '__main__':
    log_journal = SSHLogJournal()

    with open('test.log') as f:
        log_lines = f.readlines()

        for log_line in log_lines:
            log_journal.append(log_line)

    mixed_list = log_journal.get_logs_by_ip('185.190.58.151')

    for lo in mixed_list:
        print(lo)
