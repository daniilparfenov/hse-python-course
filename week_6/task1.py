"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/permutation-in-string
"""  # noqa: E501


class Solution:
    def isEqualDict(self, d1, d2):
        for key in d1:
            if d1[key] != d2[key]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = dict((letter, 0) for letter in "qwertyuiopasdfghjklzxcvbnm")
        window_freq = dict((letter, 0) for letter in "qwertyuiopasdfghjklzxcvbnm")

        for i in range(len(s1)):
            s1_freq[s1[i]] += 1
            window_freq[s2[i]] += 1

        if self.isEqualDict(s1_freq, window_freq):
            return True

        for i in range(len(s1), len(s2)):
            window_freq[s2[i - len(s1)]] -= 1
            window_freq[s2[i]] += 1
            if self.isEqualDict(s1_freq, window_freq):
                return True
        return False
