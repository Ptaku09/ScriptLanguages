import abc
import ipaddress
from typing import Optional, List, Union

from utils import get_date, get_host_name, get_pid, is_line_valid, get_message, get_ipv4s_from_log


class SSHLogEntry(metaclass=abc.ABCMeta):
    def __init__(self, line: str) -> None:
        if is_line_valid(line):
            self._line: str = line
            self.date: str = get_date(line)
            self.host_name: str = get_host_name(line)
            self.pid: str = get_pid(line)
            self.message: str = get_message(line)
        else:
            raise ValueError('Invalid line format')

    def __str__(self) -> str:
        return f'{self.date} {self.host_name} {self.pid} - {self.message}'

    def get_ipv4(self) -> Optional[ipaddress.IPv4Address]:
        ipv4s: List[str] = get_ipv4s_from_log(self.message)

        if ipv4s:
            return ipaddress.IPv4Address(ipv4s[0])
        else:
            return None

    @abc.abstractmethod
    def validate(self) -> bool:
        pass

    @property
    def has_ip(self) -> bool:
        if self.get_ipv4():
            return True

        return False

    def __repr__(self) -> str:
        return f'SSHLogEntry(_line={self._line}, date={self.date}, host_name={self.host_name}, pid={self.pid}, message={self.message})'

    def __eq__(self, other: Union[object, 'SSHLogEntry']) -> bool:
        if not isinstance(other, SSHLogEntry):
            return NotImplemented
        return self.pid == other.pid

    def __lt__(self, other: 'SSHLogEntry') -> bool:
        return int(self.pid) < int(other.pid)

    def __gt__(self, other: 'SSHLogEntry') -> bool:
        return int(self.pid) > int(other.pid)
