"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/find-all-anagrams-in-a-string
"""  # noqa: E501


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        window_freq = [0 for _ in range(26)]
        query_word_freq = [0 for _ in range(26)]
        annagrams_indeces = []

        for i in range(len(p)):
            query_word_freq[ord(p[i]) - ord("a")] += 1
            window_freq[ord(s[i]) - ord("a")] += 1

        if window_freq == query_word_freq:
            annagrams_indeces.append(0)

        for i in range(len(p), len(s)):
            window_freq[ord(s[i - len(p)]) - ord("a")] -= 1
            window_freq[ord(s[i]) - ord("a")] += 1
            if window_freq == query_word_freq:
                annagrams_indeces.append(i - len(p) + 1)
        return annagrams_indeces
