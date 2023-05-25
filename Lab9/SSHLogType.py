from abc import ABC
from typing import Optional

from SSHLogEntry import SSHLogEntry
from utils import get_user_from_log, get_port_from_log, MessageType, get_message_type


class SSHLogFailedPassword(SSHLogEntry, ABC):
    def __init__(self, line: str) -> None:
        super().__init__(line)
        self.user: str = get_user_from_log(self.message)
        self.ip: Optional[str] = self.get_ipv4()
        self.port: Optional[int] = get_port_from_log(self.message)

    def validate(self) -> bool:
        return get_message_type(self.message) == MessageType.FAILED_PASSWORD


class SSHLogAcceptedPassword(SSHLogEntry, ABC):
    def __init__(self, line: str) -> None:
        super().__init__(line)
        self.user: str = get_user_from_log(self.message)
        self.ip: Optional[str] = self.get_ipv4()
        self.port: Optional[int] = get_port_from_log(self.message)

    def validate(self) -> bool:
        return get_message_type(self.message) == MessageType.ACCEPTED_PASSWORD


class SSHLogError(SSHLogEntry, ABC):
    def __init__(self, line: str) -> None:
        super().__init__(line)
        self.ip: Optional[str] = self.get_ipv4()

    def validate(self) -> bool:
        return get_message_type(self.message) == MessageType.ERROR


class SSHLogOther(SSHLogEntry, ABC):
    def __init__(self, line: str) -> None:
        super().__init__(line)
        self.ip: Optional[str] = self.get_ipv4()

    def validate(self) -> bool:
        return True
