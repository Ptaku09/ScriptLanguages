from SSHLogFactory import log_factory


class SSHLogJournal:
    def __init__(self):
        self.logs = []

    def append(self, log):
        log_obj = log_factory.create_log(log)
        self.logs.append(log_obj)
