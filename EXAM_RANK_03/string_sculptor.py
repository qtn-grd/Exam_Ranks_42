def sculptor(text: str) -> str:

    text = text.lower()

    count = False
    result = []

    for char in text:
        if not char.isalpha():
            result.append(char)
        else:
            if not count:
                result.append(char)
                count = True
            else:
                result.append(char.upper())
                count = False

    return ''.join(result)


if __name__ == "__main__":

    print("Basic case")
    print(sculptor("Hello world"), "\n")

    print("With punctuation")
    print(sculptor("Hello, world!"), "\n")

    print("With numbers")
    print(sculptor("123abcDEF"), "\n")

    print("Mixed characters")
    print(sculptor("a-bC-dEf-ghIj"), "\n")

    print("Edge cases")
    print(sculptor("A"))
    print(sculptor(""))
    print(sculptor("12345"))
    print(sculptor("ab"))
