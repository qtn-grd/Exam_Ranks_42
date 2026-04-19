def merge_list(list1: list[int], list2: list[int]) -> list[int]:

    if not list1:
        list1 = []
    if not list2:
        list2 = []

    merged = list1 + list2

    sorted_result = sorted(merged)

    return sorted_result


if __name__ == "__main__":

    print(merge_list([1, 3, 5, -1], [0, 8, 2, 1]))
    print(merge_list([99, -22, 10, 9], []))
    print(merge_list([4, 2], [1, 3]), "\n")

    print(merge_list(None, [5, 3, 1]))
    print(merge_list([7, 6, 8], None), "\n")

    print(merge_list([], []))
    print(merge_list([1, 1, 1], [1, 1]))
    print(merge_list([-5, -2], [-3, -1]))
