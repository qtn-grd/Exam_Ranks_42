def anagram(first: str, second: str) -> bool:

    first = first.upper()
    second = second.upper()

    first = ''.join(char for char in first if char.isalpha())
    second = ''.join(char for char in second if char.isalpha())

    return sorted(first) == sorted(second)


if __name__ == "__main__":

    print(anagram("race1car", "carr1ace"), "\n")

    print(anagram("racecar", "carace"), "\n")

    print(anagram("Conversation", "Voices rant on"))
