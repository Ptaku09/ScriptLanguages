import ipaddress

from utils import get_date, get_host_name, get_pid, is_line_valid, get_message, get_ipv4s_from_log


class SSHLogEntry:
    def __init__(self, line):
        if is_line_valid(line):
            self.line = line
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


if __name__ == '__main__':
    l1 = SSHLogEntry('Mar 1 00:00:00 host sshd[123]: Invalid user user1 from 123.131.42.2')

    print(l1)
    print(l1.get_ipv4())
