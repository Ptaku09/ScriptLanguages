from itertools import islice


def make_generator(func):
    def generator():
        arg = 1
        while True:
            yield func(arg)
            arg += 1

    return generator


if __name__ == '__main__':
    def fibo(n):
        return n if n < 2 else fibo(n - 1) + fibo(n - 2)


    fibo_generator = make_generator(fibo)
    first_10_fibo = islice(fibo_generator(), 10)

    print('Fibonacci generator:')

    for i in first_10_fibo:
        print(i)

    print('------------------------')
    print('Numbers generator:')

    number_generator = make_generator(lambda n: n * 5)
    first_10_elems = islice(number_generator(), 10)

    for i in first_10_elems:
        print(i)
