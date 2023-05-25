import ipaddress
import re
from typing import Iterator, Union, List

from SSHLogFactory import log_factory
from SSHLogType import SSHLogFailedPassword, SSHLogAcceptedPassword, SSHLogError, SSHLogOther

Log = Union[SSHLogFailedPassword, SSHLogAcceptedPassword, SSHLogError, SSHLogOther]


class SSHLogJournal:
    def __init__(self) -> None:
        self.logs: List[Log] = []

    def append(self, log: str) -> None:
        log_obj: Log = log_factory.create_log(log)
        self.logs.append(log_obj)

    def get_logs_by_ip(self, ip: str) -> List[Log]:
        if re.search(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip) is None:
            raise ValueError("Invalid IP address")

        ip: ipaddress.IPv4Address = ipaddress.IPv4Address(ip)

        return [log for log in self.logs if log.ip == ip]

    def __len__(self) -> int:
        return len(self.logs)

    def __iter__(self) -> Iterator[Log]:
        return iter(self.logs)

    def __contains__(self, item: str) -> bool:
        return item in self.logs


if __name__ == '__main__':
    log_journal = SSHLogJournal()

    with open('test.log') as f:
        log1 = f.readlines()

        for log1 in log1:
            log_journal.append(log1)

    mixed_list = log_journal.get_logs_by_ip('185.190.58.151')

    for lo in mixed_list:
        print(lo)
