def sculptor(text: str) -> str:

    text = text.lower()

    count = False
    result = ""

    for char in text:
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
