import string


def acronym(words: list[string]) -> string:
    return "".join(["" if len(word[0]) == 0 else word[0] for word in words]).upper()


def median(numbers: list[int]) -> float:
    numbers.sort()

    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]


def newton_sqrt(x: float, epsilon: float) -> float:
    try:
        y = x

        while abs(y ** 2 - x) >= epsilon or y < 0:
            y = (y + x / y) / 2

        return y
    except TypeError:
        print("x and epsilon must be a number")
        exit(1)
