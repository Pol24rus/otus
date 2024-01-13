def square(value: int) -> int:
    return value ** 2


def calc_sum(a: int, b: int) -> int:
    return a + b


def main():
    a = calc_sum(2, 3)
    b = square(a)
    print(b)
     # (square(calc_sum(2, 3))))


if __name__ == "__main__":
    main()
