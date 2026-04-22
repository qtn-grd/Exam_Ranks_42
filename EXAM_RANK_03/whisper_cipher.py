def shift_alphabet(s: str, n: int) -> str:

    result = []

    for char in s:
        if char.isalpha():
            if char.islower():
                base = ord("a")
            else:
                base = ord("A")
            shifted = (ord(char) - base + n) % 26
            result.append(chr(base + shifted))
        else:
            result.append(char)

    return ''.join(result)


if __name__ == "__main__":

    print("Basic cases")
    print(shift_alphabet("abz", 1))
    print(shift_alphabet("AbZ", 1), "\n")

    print("With spaces and punctuation")
    print(shift_alphabet("Hello World!", 3), "\n")

    print("Negative shift")
    print(shift_alphabet("bca", -1), "\n")

    print("Large shift (wrap around)")
    print(shift_alphabet("abc", 26))
    print(shift_alphabet("xyz", 3), "\n")

    print("Mixed characters")
    print(shift_alphabet("Python 3.8!", 5), "\n")

    print("Edge cases")
    print(shift_alphabet("12345", 4))
    print(shift_alphabet("", 10))
