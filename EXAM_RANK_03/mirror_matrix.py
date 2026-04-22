def reverse_matrix(s: list[list[int]]) -> list[list[int]]:

    if not s:
        return []

    segment = len(s[0])

    flatted = [value for elem in s for value in elem]

    reversed = flatted[::-1]

    result = []

    for i in range(0, len(reversed), segment):
        bloc = reversed[i:i+segment]
        result.append(bloc)

    return result


if __name__ == "__main__":

    print("Basic cases")
    print(reverse_matrix([[1, 2], [3, 4]]))
    print(reverse_matrix([[1, 2, 3], [4, 5, 6]]), "\n")

    print("Single row")
    print(reverse_matrix([[1, 2, 3, 4]]), "\n")

    print("Single column")
    print(reverse_matrix([[1], [2], [3]]), "\n")

    print("Edge cases")
    print(reverse_matrix([[1]]))
    print(reverse_matrix([]), "\n")

    print("Larger matrix")
    print(reverse_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
