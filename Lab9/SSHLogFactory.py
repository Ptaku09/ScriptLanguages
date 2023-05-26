import abc
from typing import List, Union

from SSHLogEntry import SSHLogEntry
from SSHLogType import SSHLogFailedPassword, SSHLogAcceptedPassword, SSHLogError, SSHLogOther

Log = Union[SSHLogFailedPassword, SSHLogAcceptedPassword, SSHLogError, SSHLogOther]


class SSHLogCreator(abc.ABC):
    @abc.abstractmethod
    def create_log(self, line: str) -> Log:
        pass

    def validate(self, line: str) -> bool:
        log: SSHLogEntry = self.create_log(line)
        return log.validate()


class SSHLogFailedPasswordCreator(SSHLogCreator):
    def create_log(self, line: str) -> Log:
        return SSHLogFailedPassword(line)


class SSHLogAcceptedPasswordCreator(SSHLogCreator):
    def create_log(self, line: str) -> Log:
        return SSHLogAcceptedPassword(line)


class SSHLogErrorCreator(SSHLogCreator):
    def create_log(self, line: str) -> Log:
        return SSHLogError(line)


class SSHLogOtherCreator(SSHLogCreator):
    def create_log(self, line: str) -> Log:
        return SSHLogOther(line)


class SSHLogFactory:
    def __init__(self) -> None:
        self._creators: List[SSHLogCreator] = [
            SSHLogFailedPasswordCreator(),
            SSHLogAcceptedPasswordCreator(),
            SSHLogErrorCreator(),
            SSHLogOtherCreator()
        ]

    def create_log(self, line: str) -> Log:
        for creator in self._creators:
            if creator.validate(line):
                return creator.create_log(line)

        raise ValueError("Log type not found")


log_factory: SSHLogFactory = SSHLogFactory()
