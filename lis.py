from typing import List


def lis(x: List[int]) -> int:
    # A cache is used to memoize solved overlapping sub-problems.
    # The cache's max value will be the length of the LIS.
    # LIS at each element is at least one.
    cache = [1 for _ in range(len(x))]

    # Traverse the array in reverse.
    for i in range(len(x) - 1, -1, -1):
        for j in range(i + 1, len(x)):
            # If x[i] is less than the x[j] then the values are increasing.
            # Update the cache with the length of the LIS for x[i].
            # The LIS at i is either 1 or the LIS at the next element.
            if x[i] < x[j]:
                cache[i] = max(cache[i], cache[j] + 1)

    return max(cache)


if __name__ == "__main__":
    result = lis([-2, 0, 1, 2, 4, 5, -1, 2, 3, 9])
    print(result)
