from itertools import islice


def make_generator(func):
    def generator():
        arg = 1
        while True:
            yield func(arg)
            arg += 1

    return generator


def fibo(n):
    return n if n < 2 else fibo(n - 1) + fibo(n - 2)


def get_n_elems(n, func):
    return islice(make_generator(func)(), n)


if __name__ == '__main__':
    first_10_fibo = get_n_elems(10, fibo)
    print('Fibonacci generator:')

    for i in first_10_fibo:
        print(i)

    print('------------------------')
    print('Numbers generator:')

    first_10_elems = get_n_elems(10, lambda n: n * 5)

    for i in first_10_elems:
        print(i)
