def square(value: int) -> int:
    return value ** 2


def calc_sum(a: int, b: int) -> int:
    return a + b


def main():
    print(square(calc_sum(2, 3)))


if __name__ == "__main__":
    main()
