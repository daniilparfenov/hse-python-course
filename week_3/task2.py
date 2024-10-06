"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/spiral-matrix/description
"""  # noqa: E501


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        x, y = 0, 0
        dx, dy = 1, 0
        res = []

        for i in range(m * n):
            res.append(matrix[y][x])
            matrix[y][x] = "."
            if x + dx >= n or y + dy >= m or matrix[y + dy][x + dx] == ".":
                dx, dy = -dy, dx
            x += dx
            y += dy
        return res
