"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/set-matrix-zeroes/description
"""  # noqa: E501


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroesIdx = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroesIdx.append((i, j))

        for zero in zeroesIdx:
            row = zero[0]
            col = zero[1]
            for i in range(len(matrix)):
                matrix[i][col] = 0
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
