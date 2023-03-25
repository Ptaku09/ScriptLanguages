# entry_to_dict ---------------------
def entry_to_dict(log):
    return {
        "ip": log[0],
        "datetime": log[1],
        "method": log[2],
        "path": log[3],
        "protocol": log[4],
        "status code": log[5],
        "size": log[6]
    }
