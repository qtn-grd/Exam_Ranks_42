def is_palindrome(s: str) -> bool:

    cleaned = "".join(char.lower() for char in s if char.isalnum())

    return cleaned == cleaned[::-1]


if __name__ == "__main__":

    print("Valid cases")
    print(is_palindrome("madam"))
    print(is_palindrome("racecar"))
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("No 'x' in Nixon"))
    print(is_palindrome(""))
    print(is_palindrome("a"), "\n")

    print("Invalid cases")
    print(is_palindrome("hello"))
    print(is_palindrome("python"))
    print(is_palindrome("OpenAI"), "\n")

    print("Edge cases")
    print(is_palindrome("12321"))
    print(is_palindrome("12345"))
    print(is_palindrome("Able was I ere I saw Elba"))
