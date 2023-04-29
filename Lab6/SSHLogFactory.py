import abc

import SSHLogEntry
from SSHLogType import SSHLogFailedPassword, SSHLogAcceptedPassword, SSHLogError, SSHLogOther


class SSHLogCreator(abc.ABC):
    @abc.abstractmethod
    def create_log(self, line):
        pass

    def validate(self, line):
        log = self.create_log(line)
        return log.validate()


class SSHLogFailedPasswordCreator(SSHLogCreator):
    def create_log(self, line) -> SSHLogEntry:
        return SSHLogFailedPassword(line)


class SSHLogAcceptedPasswordCreator(SSHLogCreator):
    def create_log(self, line) -> SSHLogEntry:
        return SSHLogAcceptedPassword(line)


class SSHLogErrorCreator(SSHLogCreator):
    def create_log(self, line) -> SSHLogEntry:
        return SSHLogError(line)


class SSHLogOtherCreator(SSHLogCreator):
    def create_log(self, line) -> SSHLogEntry:
        return SSHLogOther(line)
