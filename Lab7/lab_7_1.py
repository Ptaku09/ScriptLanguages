import string


def acronym(words: list[string]) -> string:
    return "".join(["" if len(word[0]) == 0 else word[0] for word in words]).upper()
