"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/smallest-integer-divisible-by-k/description
"""  # noqa: E501


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        n = 1
        c = 1
        while n % k != 0:
            n = (10 * n + 1) % k
            c += 1
        return c
