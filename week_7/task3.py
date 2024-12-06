"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters
"""  # noqa: E501

from collections import defaultdict


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        letter_freqs = defaultdict(int)
        for letter in s:
            letter_freqs[letter] += 1

        for i, letter in enumerate(s):
            if letter_freqs[letter] < k:
                return max(
                    self.longestSubstring(s[:i], k),
                    self.longestSubstring(s[i + 1 :], k),
                )
        return len(s)
