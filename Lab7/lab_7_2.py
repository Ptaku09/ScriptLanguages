from typing import Callable, Iterable


def forall(pred: Callable[[any], bool], iterable: Iterable) -> bool:
    try:
        return all(pred(x) for x in iterable)
    except TypeError:
        print("you should provide a predicate and an iterable")
        exit(1)


def exists(pred: Callable[[any], bool], iterable: Iterable) -> bool:
    try:
        return any(pred(x) for x in iterable)
    except TypeError:
        print("you should provide a predicate and an iterable")
        exit(1)


def atleast(n: int, pred: Callable[[any], bool], iterable: Iterable) -> bool:
    try:
        return sum(1 for x in iterable if pred(x)) >= n
    except TypeError:
        print("you should provide a number, a predicate and an iterable")
        exit(1)


def atmost(n: int, pred: Callable[[any], bool], iterable: Iterable) -> bool:
    try:
        return sum(1 for x in iterable if pred(x)) <= n
    except TypeError:
        print("you should provide a number, a predicate and an iterable")
        exit(1)
