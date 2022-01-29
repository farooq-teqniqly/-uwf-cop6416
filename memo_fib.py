from typing import List

computed: List[int] = [0, 1]


def fib(n: int) -> int:
    print(f"n => {n}")
    if n < len(computed):
        return computed[n]

    result = fib(n - 1) + fib(n - 2)

    computed.append(result)
    print(f"Result => {result}. Len = {len(computed)}")

    return result


if __name__ == "__main__":
    print(fib(600))
