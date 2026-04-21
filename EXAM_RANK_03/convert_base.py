def convert_base(num: str, from_base: int, to_base: int) -> str:

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not 2 <= from_base <= 36:
        return "Error / invalid input"
    if not 2 <= to_base <= 36:
        return "Error / invalid input"

    try:
        num = num.upper()
        value = 0

        for char in num:
            digit = digits.index(char)
            if digit >= from_base:
                return "Error / invalid input"
            value = value * from_base + digit

        if value == 0:
            return "0"

        result = ""

        while value > 0:
            result = result + digits[value % to_base]
            value = value // to_base

        return result[::-1]

    except Exception:
        return "Error / invalid input"


if __name__ == "__main__":

    print(convert_base("1010", 2, 10))
    print(convert_base("10", 10, 2))
    print(convert_base("1A", 16, 10))
    print(convert_base("26", 10, 16), "\n")

    print(convert_base("123", 10, 10), "\n")

    print(convert_base("0", 10, 2))
    print(convert_base("000", 2, 10), "\n")

    print(convert_base("ZZZ", 36, 10))
    print(convert_base("46655", 10, 36), "\n")

    print(convert_base("A", 16, 10))
    print(convert_base("F", 16, 10), "\n")

    print(convert_base("1F4", 16, 10))
    print(convert_base("500", 10, 16), "\n")

    print(convert_base("2", 2, 10))
    print(convert_base("G", 16, 10))
