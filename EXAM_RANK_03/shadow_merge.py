def merge_list(list1: list[int], list2: list[int]) -> list[int]:

    if not list1:
        list1 = []
    if not list2:
        list2 = []

    merged = list1 + list2

    return sorted(merged)


if __name__ == "__main__":

    print("Basic cases")
    print(merge_list([1, 3, 5, -1], [0, 8, 2, 1]))
    print(merge_list([99, -22, 10, 9], []), "\n")

    print("Both lists non-empty")
    print(merge_list([4, 2], [1, 3]), "\n")

    print("One list is None")
    print(merge_list(None, [5, 3, 1]))
    print(merge_list([7, 6, 8], None), "\n")

    print("Edge cases")
    print(merge_list([], []))
    print(merge_list([1, 1, 1], [1, 1]))
    print(merge_list([-5, -2], [-3, -1]))
