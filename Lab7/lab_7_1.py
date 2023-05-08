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
        if len(numbers) % 2 == 0:
            return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
        else:
            return numbers[len(numbers) // 2]
    except TypeError:
        print("numbers must be a list of numbers")
        exit(1)


def newton_sqrt(x: float, epsilon: float) -> float:
    try:
        y = x

        while abs(y ** 2 - x) >= epsilon or y < 0:
            y = (y + x / y) / 2

        return y
    except TypeError:
        print("x and epsilon must be a number")
        exit(1)
