import time
from functools import cache
from itertools import islice

from lab_7_4 import make_generator, fibo


@cache
def make_generator_mem(func):
    mem = cache(func)
    return make_generator(mem)


def get_n_elems(n, func):
    return islice(make_generator_mem(func)(), n)


if __name__ == '__main__':
    start = time.time() * 1000
    get_n_elems(10, fibo)
    print(f"1. {round(time.time() * 1000 - start, 4)}")

    start = time.time() * 1000
    get_n_elems(10, fibo)
    print(f"2. {round(time.time() * 1000 - start, 4)}")
