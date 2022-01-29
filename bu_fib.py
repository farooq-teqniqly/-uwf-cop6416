def fib(n: int) -> int:
    n_minus_2 = 0
    n_minus_1 = 1
    result = 0

    while True:
        n = n - 1

        if n <= 0:
            break

        result = n_minus_1 + n_minus_2
        n_minus_2 = n_minus_1
        n_minus_1 = result

    return result


if __name__ == "__main__":
    print(fib(600))
