import re

from SSHLogJournal import SSHLogJournal


class SSHUser:
    def __init__(self, username, last_login):
        self.username = username
        self.last_login = last_login

    def validate(self):
        return re.search(r'^[a-z_][a-z0-9_-]{0,31}$', self.username) is not None


if __name__ == '__main__':
    log_journal = SSHLogJournal()

    with open('test.log') as f:
        log1 = f.readlines()

        for log1 in log1:
            log_journal.append(log1)

    mixed_list = log_journal.get_logs_by_ip('183.62.140.253')

    u1 = SSHUser('user1', 'Mar 1 00:00:00')
    u2 = SSHUser('user2', 'Mar 1 00:00:00')
    u3 = SSHUser('user3', 'Mar 1 00:00:00')

    mixed_list += [u1, u2, u3]

    for lo in mixed_list:
        print(f'{lo.__class__.__name__:23s} {lo.validate()}')
