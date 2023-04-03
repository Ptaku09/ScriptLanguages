# entry_to_dict ---------------------
import functools

from lab_2 import read_log


def entry_to_dict(entry):
    return {
        "ip": entry[0],
        "datetime": entry[1],
        "method": entry[2],
        "path": entry[3],
        "protocol": entry[4],
        "status code": entry[5],
        "size": entry[6]
    }


# log_to_dict -----------------------
def log_to_dict(log):
    dictionary = {}

    for e in log:
        if e[0] not in dictionary:
            dictionary[e[0]] = [entry_to_dict(e)]
        else:
            dictionary[e[0]].append(entry_to_dict(e))

    return dictionary


# get_addrs -------------------------
def get_addrs(dictionary):
    return list(dictionary)


# print_dict_entry_dates
def print_dict_entry_dates(dictionary):
    for key, value in dictionary.items():
        print(f"ip / name: {key}")
        print(f"requests: {len(value)}")

        value.sort(key=lambda x: x["datetime"])

        print(f"first request: {value[0]['datetime']}")
        print(f"last request: {value[-1]['datetime']}")

        founded_302s = functools.reduce(lambda acc, x: acc + 1 if x["status code"] == 302 else acc, value, 0)

        print(f"ratio of 302s: {round(founded_302s / len(value), 2)}")
        print("\n--------------------------------------\n")


if __name__ == "__main__":
    t = read_log()
    d = log_to_dict(t)
    print_dict_entry_dates(d)
