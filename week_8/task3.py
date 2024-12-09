"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters
"""  # noqa: E501

from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = defaultdict(int)
        n = len(s)
        left, right, result = 0, 0, 0

        for right in range(n):
            freq[s[right]] += 1
            while freq["a"] and freq["b"] and freq["c"]:
                result += n - right
                freq[s[left]] -= 1
                left += 1
        return result
