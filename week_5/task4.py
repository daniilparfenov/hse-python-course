"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/ugly-number-ii/description
"""  # noqa: E501


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uNumbers = [1]
        x2 = x3 = x5 = 0

        while len(uNumbers) < n:
            nextX2 = uNumbers[x2] * 2
            nextX3 = uNumbers[x3] * 3
            nextX5 = uNumbers[x5] * 5

            next = min(nextX2, nextX3, nextX5)
            uNumbers.append(next)
            if next == nextX2:
                x2 += 1
            if next == nextX3:
                x3 += 1
            if next == nextX5:
                x5 += 1

        return uNumbers[n - 1]
