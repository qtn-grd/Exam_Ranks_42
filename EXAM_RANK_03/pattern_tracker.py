def pattern_tracker(s: str) -> int:

    count = 0
    for i in range(1, len(s)):
        if s[i].isdigit() and s[i - 1].isdigit():
            if int(s[i - 1]) == int(s[i]) - 1:
                count += 1
    return count


if __name__ == "__main__":

    print(pattern_tracker("123a345"), "\n")

    print(pattern_tracker("1a2b3c4d5"), "\n")

    print(pattern_tracker(
        "12asd34hkh45kjhj56jhj67kjhjh78kjhjh89kjhkhj110"), "\n")

    print(pattern_tracker(""), "\n")

    print(pattern_tracker("7"), "\n")

    print(pattern_tracker("111111"), "\n")

    print(pattern_tracker("012345"), "\n")

    print(pattern_tracker("98"))
