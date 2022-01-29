from typing import List


def lcs_length(x: List[int], y: List[int]) -> int:
    matrix = [[0 for i in range(len(x))] for j in range(len(y))]
    max_value = 0

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if x[i - 1] == y[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i][j - 1], matrix[i - 1][j])

        if matrix[i][j] > max_value:
            max_value = matrix[i][j]

    return max_value


if __name__ == "__main__":
    result = lcs_length([1, 0, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 0, 1, 1, 0])
