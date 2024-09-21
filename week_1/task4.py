"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=string
"""  # noqa: E501


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        isSymbolVisited = dict()
        rightPtr = 0
        leftPtr = 0
        maxSubstringLength = -1

        while rightPtr < len(s):
            while isSymbolVisited.get(s[rightPtr]):
                isSymbolVisited[s[leftPtr]] = False
                leftPtr += 1
            maxSubstringLength = max(maxSubstringLength, rightPtr - leftPtr + 1)
            isSymbolVisited[s[rightPtr]] = True
            rightPtr += 1

        return maxSubstringLength
