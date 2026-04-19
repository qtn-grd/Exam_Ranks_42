def sculptor(to_sculpt: str) -> str:

    low = to_sculpt.lower()

    count = False
    result = ""

    for char in low:
        if not char.isalpha():
            result += char
        else:
            if not count:
                result += char
                count = True
            else:
                char = char.upper()
                result += char
                count = False

    return result


if __name__ == "__main__":

    print(sculptor("Hello world"), "\n")

    print(sculptor("Hello, world!"), "\n")

    print(sculptor("123abcDEF"), "\n")

    print(sculptor("a-bC-dEf-ghIj"), "\n")

    print(sculptor(""))
    print(sculptor("12345"))
    print(sculptor("A"))
    print(sculptor("ab"))
