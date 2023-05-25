import abc
import ipaddress

from utils import get_date, get_host_name, get_pid, is_line_valid, get_message, get_ipv4s_from_log


class SSHLogEntry(metaclass=abc.ABCMeta):
    def __init__(self, line):
        if is_line_valid(line):
            self._line = line
            self.date = get_date(line)
            self.host_name = get_host_name(line)
            self.pid = get_pid(line)
            self.message = get_message(line)
        else:
            raise ValueError('Invalid line format')

    def __str__(self):
        return f'{self.date} {self.host_name} {self.pid} - {self.message}'

    def get_ipv4(self):
        ipv4s = get_ipv4s_from_log(self.message)

        if ipv4s:
            return ipaddress.IPv4Address(ipv4s[0])
        else:
            return None

    @abc.abstractmethod
    def validate(self):
        pass

    @property
    def has_ip(self):
        if self.get_ipv4():
            return True

        return False

    def __repr__(self):
        return f'SSHLogEntry(_line={self._line}, date={self.date}, host_name={self.host_name}, pid={self.pid}, message={self.message})'

    def __eq__(self, other):
        return self.pid == other.pid

    def __lt__(self, other):
        return int(self.pid) < int(other.pid)

    def __gt__(self, other):
        return int(self.pid) > int(other.pid)


if __name__ == '__main__':
    l1 = SSHLogEntry(
        'Dec 10 09:09:56 LabSZ sshd[24421]: Failed password for invalid user admin from 185.190.58.151 port 41650 ssh2')
    l2 = SSHLogEntry('Dec 10 09:10:03 LabSZ sshd[24421]: pam_unix(sshd:auth): check pass; user unknown')

    print(repr(l1))
    print(repr(l2))
    print(l1 == l2)
    print(l1 < l2)
    print(l1 > l2)
