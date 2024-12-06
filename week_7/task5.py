"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-repeating-character-replacement
"""  # noqa: E501


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        n = len(s)

        for letter in "QWERTYUIOPASDFGHJKLZXCVBNM":
            start, end, replaced = 0, 0, 0
            while end < n:
                if s[end] == letter:
                    end += 1
                elif replaced < k:
                    end += 1
                    replaced += 1
                elif s[start] == letter:
                    start += 1
                else:
                    start += 1
                    replaced -= 1
                res = max(res, end - start)
        return res
