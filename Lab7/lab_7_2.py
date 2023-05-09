def forall(pred, iterable):
    try:
        return all(pred(x) for x in iterable)
    except TypeError:
        print("you should provide a predicate and an iterable")
        exit(1)


def exists(pred, iterable):
    try:
        return any(pred(x) for x in iterable)
    except TypeError:
        print("you should provide a predicate and an iterable")
        exit(1)
       