"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/description
"""  # noqa: E501


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindromeStart = longestPalindromeEnd = -1
        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                if (s[start:end] == s[start:end][::-1]) and (
                    end - start > longestPalindromeEnd - longestPalindromeStart
                ):
                    longestPalindromeStart = start
                    longestPalindromeEnd = end

        return s[longestPalindromeStart:longestPalindromeEnd]
