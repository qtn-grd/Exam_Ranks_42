def sort_string(to_sort: list[str]) -> list[str]:

    voy = set("aeiouAEIOU")

    return sorted(to_sort, key=lambda word: (
            sum(1 for char in word if char in voy), len(word), word)
    )


if __name__ == "__main__":

    print(sort_string(["apple", "bat", "car", "ae", "b"]), "\n")

    print(sort_string(["dog", "cat", "hi", "a"]), "\n")

    print(sort_string(["bat", "cat", "ant"]), "\n")

    print(sort_string(["Apple", "banana", "Kiwi", "grape"]), "\n")

    print(sort_string([]), "\n")

    print(sort_string(["a", "e", "i", "o", "u"]), "\n")

    print(sort_string(["bbb", "ccc", "ddd"]), "\n")
