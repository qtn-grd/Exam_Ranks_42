def shift_alphabet(to_shift: str, notch: int) -> str:

    result = []

    for char in to_shift:
        if char.isalpha():
            if char.islower():
                base = ord("a")
            else:
                base = ord("A")
            shifted = (ord(char) - base + notch) % 26
            result.append(chr(base + shifted))
        else:
            result.append(char)

    return ''.join(result)


if __name__ == "__main__":

    print(shift_alphabet("abz", 1))
    print(shift_alphabet("AbZ", 1))
    print(shift_alphabet("abc", 26))
    print(shift_alphabet("xyz", 3), "\n")

    print(shift_alphabet("bca", -1), "\n")

    print(shift_alphabet("Hello World!", 3))
    print(shift_alphabet("Python 3.8!", 5), "\n")

    print(shift_alphabet("", 10))
    print(shift_alphabet("12345", 4))
