def twister(nums: list, n: int) -> list:

    if not nums:
        return []

    n = n % len(nums)

    return nums[-n:] + nums[:-n]


if __name__ == "__main__":

    print("Basic cases")
    print(twister([1, 2, 3, 4, 5], 2))
    print(twister([4, 2, 1, -1, 'a'], 4), "\n")

    print("Rotation equal to length")
    print(twister([1, 2, 3], 3), "\n")

    print("Rotation greater than length")
    print(twister([1, 2, 3], 5), "\n")

    print("Negative rotation (left rotation)")
    print(twister([1, 2, 3, 4], -1), "\n")

    print("Edge cases")
    print(twister([], 3))
    print(twister([1], 10))
