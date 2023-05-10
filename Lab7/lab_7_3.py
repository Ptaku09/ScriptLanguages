import string
from random import sample

from lab_7_2 import forall


class PasswordGenerator:
    def __init__(self, length: int, charset=tuple(string.ascii_letters + string.digits), count=10):
        self.length = length
        self.charset = charset
        self.count = count
        self.validate()

    def validate(self):
        if not isinstance(self.length, int):
            raise TypeError("length must be an integer")
        if not isinstance(self.charset, list) and not isinstance(self.charset, tuple):
            raise TypeError("charset must be a list or tuple")
        if not isinstance(self.count, int):
            raise TypeError("count must be an integer")
        if self.length < 1:
            raise ValueError("length must be greater than 0")
        if self.count < 1:
            raise ValueError("count must be greater than 0")
        if not forall(lambda x: isinstance(x, str), self.charset):
            raise TypeError("charset must be a list of strings")
        if not forall(lambda x: len(x) == 1, self.charset):
            raise ValueError("charset must be a list of single character strings")

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        self.count -= 1

        return "".join(sample(self.charset, self.length))


if __name__ == '__main__':
    test = PasswordGenerator(20, tuple(string.ascii_letters + string.digits + string.punctuation), 10)

    for password in test:
        print(password)

    print(next(test))
