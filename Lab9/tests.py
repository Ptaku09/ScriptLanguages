import ipaddress

import pytest as pytest

from SSHLogJournal import SSHLogJournal
from SSHLogType import SSHLogAcceptedPassword, SSHLogFailedPassword, SSHLogError, SSHLogOther


@pytest.mark.parametrize(
    'line, expected',
    [
        (
                'Dec 10 06:55:46 LabSZ sshd[24200]: reverse mapping checking getaddrinfo for ns.marryaldkfaczcz.com [',
                'Dec 10 06:55:46'
        ),
        (
                'Dec 10 07:28:31 LabSZ sshd[24269]: pam_unix(sshd:auth): authentication failure; user=root',
                'Dec 10 07:28:31'
        ),
        (
                'Dec 10 08:24:43 LabSZ sshd[24363]: pam_unix(sshd:auth): check pass; user unknown',
                'Dec 10 08:24:43'
        ),
        (
                'Dec 10 09:11:24 LabSZ sshd[24437]: pam_unix(sshd:auth): check pass; user unknown',
                'Dec 10 09:11:24'
        ),
        (
                'Dec 10 10:57:56 LabSZ sshd[25087]: Received disconnect from 183.62.140.253: 11: Bye Bye [preauth]',
                'Dec 10 10:57:56'
        )
    ]
)
def test_extract_date(line, expected):
    log_entry = SSHLogAcceptedPassword(line)

    assert log_entry.date == expected


@pytest.mark.parametrize(
    'line, expected',
    [
        (
                'Dec 10 10:57:47 LabSZ sshd[25077]: Failed password for root from 183.62.140.253 port 42836 ssh2',
                ipaddress.IPv4Address('183.62.140.253')
        ),
        (
                'Dec 10 09:12:10 LabSZ sshd[24455]: Failed password for invalid user admin from 185.190.58.151 port 49948 ssh2',
                ipaddress.IPv4Address('185.190.58.151')
        )
    ]
)
def test_extract_ip(line, expected):
    log_entry = SSHLogAcceptedPassword(line)

    assert log_entry.ip == expected


@pytest.mark.parametrize(
    'line, expected',
    [
        (
                'Dec 10 10:57:47 LabSZ sshd[25077]: Failed password for root from 993.62.140.253 port 42836 ssh2',
                None
        ),
        (
                'Dec 10 09:12:10 LabSZ sshd[24455]: Failed password for invalid user admin from 777.888.23.51 port 49948 ssh2',
                None
        )
    ]
)
def test_extract_ip_invalid(line, expected):
    log_entry = SSHLogAcceptedPassword(line)

    assert log_entry.ip == expected


@pytest.mark.parametrize(
    'line, expected',
    [
        (
                'Dec 10 10:57:47 LabSZ sshd[25077]: Failed password for root from',
                None
        ),
        (
                'Dec 10 09:12:10 LabSZ sshd[24455]: Failed password for invalid user admin from',
                None
        )
    ]
)
def test_extract_ip_none(line, expected):
    log_entry = SSHLogAcceptedPassword(line)

    assert log_entry.ip == expected


@pytest.mark.parametrize(
    'line, expected',
    [
        (
                'Dec 10 09:32:20 LabSZ sshd[24680]: Accepted password for fztu from 119.137.62.142 port 49116 ssh2',
                SSHLogAcceptedPassword
        ),
        (
                'Dec 10 09:12:10 LabSZ sshd[24455]: Failed password for invalid user admin from 185.190.58.151 port 49948 ssh2',
                SSHLogFailedPassword
        ),
        (
                'Dec 10 07:51:15 LabSZ sshd[24324]: error: Received disconnect from 195.154.37.122: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]',
                SSHLogError
        ),
        (
                'Dec 10 10:57:56 LabSZ sshd[25087]: Received disconnect from',
                SSHLogOther
        )
    ]
)
def test_factory(line, expected):
    log_journal = SSHLogJournal()
    log_journal.append(line)

    assert isinstance(log_journal.logs[-1], expected)
