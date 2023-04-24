from lab_6_1 import SSHLogEntry
from utils import get_user_from_log, get_port_from_log


class SSHLogFailedPassword(SSHLogEntry):
    def __init__(self, line):
        super().__init__(line)
        self.user = get_user_from_log(super().message)
        self.ip = super().get_ipv4()
        self.port = get_port_from_log(super().message)


class SSHLogAcceptedPassword(SSHLogEntry):
    def __init__(self, line):
        super().__init__(line)
        self.user = get_user_from_log(super().message)
        self.ip = super().get_ipv4()
        self.port = get_port_from_log(super().message)


class SSHLogError(SSHLogEntry):
    def __init__(self, line):
        super().__init__(line)
        self.ip = super().get_ipv4()


class SSHLogOther(SSHLogEntry):
    def __init__(self, line):
        super().__init__(line)
