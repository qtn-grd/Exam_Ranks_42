def reverse_matrix(matrix: list[list[int]]) -> list[list[int]]:

    if not matrix:
        return []

    segment = len(matrix[0])

    matrix_flatted = [value for elem in matrix for value in elem]

    matrix_reversed = matrix_flatted[::-1]

    result = []

    for i in range(0, len(matrix_reversed), segment):
        bloc = matrix_reversed[i:i+segment]
        result.append(bloc)

    return result


if __name__ == "__main__":

    print(reverse_matrix([[1, 2], [3, 4]]), "\n")

    print(reverse_matrix([[1, 2, 3], [4, 5, 6]]), "\n")

    print(reverse_matrix([[1, 2, 3, 4]]), "\n")

    print(reverse_matrix([[1], [2], [3]]), "\n")

    print(reverse_matrix([[1]]), "\n")

    print(reverse_matrix([]), "\n")

    print(reverse_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
