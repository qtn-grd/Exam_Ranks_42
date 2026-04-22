def sort_string(tlist: list[str]) -> list[str]:

    voy = set("aeiouAEIOU")

    return sorted(tlist, key=lambda word: (
            sum(1 for char in word if char in voy), len(word), word)
    )


if __name__ == "__main__":

    print("Basic cases")
    print(sort_string(["apple", "bat", "car", "ae", "b"]), "\n")

    print("Same vowel count, different lengths")
    print(sort_string(["dog", "cat", "hi", "a"]), "\n")

    print("Same vowel count and length -> lexicographical order")
    print(sort_string(["bat", "cat", "ant"]), "\n")

    print("Mixed uppercase and lowercase")
    print(sort_string(["Apple", "banana", "Kiwi", "grape"]), "\n")

    print("Edge cases")
    print(sort_string([]), "\n")

    print("Already sorted")
    print(sort_string(["a", "e", "i", "o", "u"]), "\n")

    print("No vowels, same length -> lexicographical order")
    print(sort_string(["bbb", "ccc", "ddd"]), "\n")
