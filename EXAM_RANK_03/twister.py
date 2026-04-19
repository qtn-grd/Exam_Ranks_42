def twister(arr: list, round: int) -> list[int]:

    if not arr:
        return []

    length = len(arr)

    round = round % length

    result = arr[-round:] + arr[:-round]

    return result


if __name__ == "__main__":

    print(twister([1, 2, 3, 4, 5], 2))
    print(twister([4, 2, 1, -1, 'a'], 4))
    print(twister([1, 2, 3], 3), "\n")

    print(twister([1, 2, 3], 5), "\n")

    print(twister([1, 2, 3, 4], -1), "\n")

    print(twister([], 3))
    print(twister([1], 10))
