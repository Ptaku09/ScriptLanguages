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


def atleast(n, pred, iterable):
    try:
        return sum(1 for x in iterable if pred(x)) >= n
    except TypeError:
        print("you should provide a number, a predicate and an iterable")
        exit(1)


def atmost(n, pred, iterable):
    try:
        return sum(1 for x in iterable if pred(x)) <= n
    except TypeError:
        print("you should provide a number, a predicate and an iterable")
        exit(1)
       