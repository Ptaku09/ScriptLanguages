import datetime
import re

import my_utils as mu


# read_log --------------------------------------
def read_log():
    list_of_tuples = []

    while True:
        try:
            line = input()

            if not mu.is_line_valid(line):
                raise ValueError("Invalid line")

            untyped_tuple = split_line(line)
            typed_tuple = type_tuple(untyped_tuple)
            list_of_tuples.append(typed_tuple)

        except EOFError:
            break

    return list_of_tuples


def split_line(line):
    return mu.get_address(line), mu.get_date(line), mu.get_request_method(line), mu.get_path(line), mu.get_protocol(
        line), mu.get_response_status(line), mu.get_response_size(line)


def type_tuple(untyped_tuple):
    return untyped_tuple[0], datetime.datetime.strptime(untyped_tuple[1], "%d/%b/%Y:%H:%M:%S %z"), untyped_tuple[2], \
        untyped_tuple[3], untyped_tuple[4], int(untyped_tuple[5]), int(untyped_tuple[6])


# sort_log --------------------------------------
def sort_log(log, index):
    try:
        if index < 0 or index >= len(log[0]):
            raise ValueError(f"Key must be in range 0-{len(log[0]) - 1}")

        return sorted(log, key=lambda x: x[index])
    except ValueError as e:
        print(e)
        return log


# get_entries_by_addr ---------------------------
def get_entries_by_addr(log, addr):
    try:
        if not re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", addr) and not re.search(r"^\w+\S+(\.\w{1,6})$", addr):
            raise ValueError("Invalid address")

        return [e for e in log if e[0] == addr]
    except ValueError as e:
        print(e)
        return []


# get_entries_by_code ---------------------------
def get_entries_by_code(log, code):
    try:
        if not code >= 100 and code <= 511:
            raise ValueError("Invalid code")

        return [e for e in log if e[5] == code]
    except ValueError as e:
        print(e)
        return []


# get_failed_reads ------------------------------
def get_failed_reads(log, concat=False):
    client_errors = [e for e in log if 400 <= e[5] < 500]
    server_errors = [e for e in log if 500 <= e[5] <= 511]

    if concat:
        return client_errors + server_errors

    return client_errors, server_errors


# get_entries_by_extension ----------------------
def get_entries_by_extension(log, extension):
    return [e for e in log if e[3].endswith(f".{extension}")]


if __name__ == '__main__':
    tuples = read_log()
    # sorted_list = sort_log(tuples, 12)
    # founded_addresses = get_entries_by_addr(tuples, 'ppp160.iadfw.net')
    # founded_codes = get_entries_by_code(tuples, 500)
    # failed_reads = get_failed_reads(tuples, True)
    founded_extensions = get_entries_by_extension(tuples, 'jpg')

    for i in range(10):
        print(founded_extensions[i])

    # for i in range(10):
    #     print(sorted_list[i])
    #
    # for entry in founded_addresses:
    #     print(entry)
