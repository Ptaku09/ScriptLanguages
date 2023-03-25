# entry_to_dict ---------------------


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
