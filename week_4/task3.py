"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/group-anagrams/description
"""  # noqa: E501


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for word in strs:
            key = "".join(sorted(word))
            if anagrams.get(key) is None:
                anagrams[key] = [word]
            else:
                anagrams[key].append(word)
        return anagrams.values()
