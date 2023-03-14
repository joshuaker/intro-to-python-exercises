# Write your solution here


def no_vowels(
    _string_: str
    ):
    VOWELS = ['a','e','i','o','u']

    string_save = _string_
    for item in VOWELS:
        _string_ = _string_.replace(item, '')
    return _string_


if __name__ == "__main__":
    print(no_vowels("abc"))
