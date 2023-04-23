import logging
import sys

from lab_5_1 import read_ssh_logs, line_to_dict
from lab_5_2 import get_message_type, MessageType


def level_to_type(level):
    if level == 'd':
        return logging.DEBUG

    if level == 'i':
        return logging.INFO

    if level == 'w':
        return logging.WARNING

    if level == 'e':
        return logging.ERROR

    if level == 'c':
        return logging.CRITICAL


def configure_logger(level=logging.DEBUG):
    logger = logging.getLogger()
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s - %(message)s')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)
    stdout_handler.addFilter(lambda record: record.levelno < logging.ERROR)

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.ERROR)
    stderr_handler.setFormatter(formatter)

    logger.addHandler(stdout_handler)
    logger.addHandler(stderr_handler)


def get_logger(level='d'):
    configure_logger(level_to_type(level))

    def logger(log):
        dict_log = line_to_dict(log)
        message_type = get_message_type(dict_log['message'])

        logging.debug(f'Read bytes: {len(log.encode("utf-8"))}')

        if message_type == MessageType.SUCCESSFUL_LOGGING.value:
            logging.info(MessageType.SUCCESSFUL_LOGGING.value)

        if message_type == MessageType.CONNECTION_CLOSED.value:
            logging.info(MessageType.CONNECTION_CLOSED.value)

        if message_type == MessageType.FAILED_LOGGING.value:
            logging.warning(MessageType.FAILED_LOGGING.value)

        if message_type == MessageType.WRONG_PASSWORD.value:
            logging.error(MessageType.WRONG_PASSWORD.value)

        if message_type == MessageType.WRONG_USERNAME.value:
            logging.error(MessageType.WRONG_USERNAME.value)

        if message_type == MessageType.BREAK_IN_ATTEMPT.value:
            logging.critical(MessageType.BREAK_IN_ATTEMPT.value)

    return logger


if __name__ == '__main__':
    lines = read_ssh_logs('/Users/mateusz/Desktop/Studia/Semestr IV/[L] Języki skrytpowe/Lab5/test.log')

    log_message = get_logger('d')

    for li in lines:
        log_message(li)
