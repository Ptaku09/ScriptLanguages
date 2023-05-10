import functools
import inspect
import logging
import time

formatter = logging.Formatter('\x1b[33;20m%(asctime)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def log(level):
    def decorator(func_or_class):
        @functools.wraps(func_or_class)
        def wrapper(*args, **kwargs):
            if inspect.isclass(func_or_class):
                start_time = time.time()
                logger.log(level, f"Creating an instance of {func_or_class.__name__}")
                instance = func_or_class(*args, **kwargs)
                duration = time.time() - start_time
                logger.log(level,
                           f"Finished creating an instance of {func_or_class.__name__} in {duration:.6f} seconds")
                return instance
            else:
                start_time = time.time()
                logger.log(level, f"Calling function {func_or_class.__name__} with args {args} and kwargs {kwargs}")
                result = func_or_class(*args, **kwargs)
                duration = time.time() - start_time
                logger.log(level,
                           f"Finished calling function {func_or_class.__name__} in {duration:.6f} seconds; result: {result}")
                return result

        return wrapper

    return decorator


@log(logging.INFO)
def add(a, b):
    return a + b


@log(logging.DEBUG)
class MyClass:
    def __init__(self, name):
        for i in range(100000000):
            pass
        self.name = name


if __name__ == '__main__':
    res = add(2, 3)
    my_obj = MyClass("Example")
