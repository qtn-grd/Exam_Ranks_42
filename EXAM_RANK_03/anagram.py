def anagram(s: str, t: str) -> bool:

    s = ''.join(char.upper() for char in s if char.isalpha())
    t = ''.join(char.upper() for char in t if char.isalpha())

    return sorted(s) == sorted(t)


if __name__ == "__main__":

    print(anagram("race1car", "carr1ace"), "\n")

    print(anagram("racecar", "carace"), "\n")

    print(anagram("Conversation", "Voices rant on"))
