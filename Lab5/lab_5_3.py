import logging
import sys

from lab_5_1 import read_ssh_logs, line_to_dict
from lab_5_2 import get_message_type, MessageType

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s - %(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.ERROR)
stderr_handler.setFormatter(formatter)

logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)


def log_message(log):
    dict_log = line_to_dict(log)
    message_type = get_message_type(dict_log['message'])

    logger.debug(f'Read bytes: {len(log.encode("utf-8"))}')

    if message_type == MessageType.SUCCESSFUL_LOGGING.value:
        logger.info(MessageType.SUCCESSFUL_LOGGING.value)

    if message_type == MessageType.CONNECTION_CLOSED.value:
        logger.info(MessageType.CONNECTION_CLOSED.value)

    if message_type == MessageType.FAILED_LOGGING.value:
        logger.warning(MessageType.FAILED_LOGGING.value)

    if message_type == MessageType.WRONG_PASSWORD.value:
        logger.error(MessageType.WRONG_PASSWORD.value)

    if message_type == MessageType.WRONG_USERNAME.value:
        logger.error(MessageType.WRONG_USERNAME.value)

    if message_type == MessageType.BREAK_IN_ATTEMPT.value:
        logger.critical(MessageType.BREAK_IN_ATTEMPT.value)


if __name__ == '__main__':
    lines = read_ssh_logs('/Users/mateusz/Desktop/Studia/Semestr IV/[L] Języki skrytpowe/Lab5/test.log')

    for li in lines:
        log_message(li)
