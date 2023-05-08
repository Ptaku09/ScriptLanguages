import string


def acronym(words: list[string]) -> string:
    try:
        return "".join(["" if len(word) == 0 else word[0] for word in words]).upper()
    except TypeError:
        print("words must be a list of strings")
        exit(1)


def median(numbers: list[int]) -> float:
    try:
        numbers.sort()

        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2 if len(numbers) % 2 == 0 else numbers[
            len(numbers) // 2]
    except TypeError:
        print("numbers must be a list of numbers")
        exit(1)


def newton_sqrt(x: float, epsilon: float) -> float:
    try:
        def newton_sqrt_rec(y: float) -> float:
            return y if abs(y ** 2 - x) < epsilon and y >= 0 else newton_sqrt_rec((y + x / y) / 2)

        return newton_sqrt_rec(x)
    except TypeError:
        print("x and epsilon must be a number")
        exit(1)
