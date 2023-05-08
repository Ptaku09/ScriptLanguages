import string


def acronym(words: list[string]) -> string:
    return "".join(["" if len(word[0]) == 0 else word[0] for word in words]).upper()


def median(numbers: list[int]) -> float:
    numbers.sort()

    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    else:
        return numbers[len(numbers) // 2]
