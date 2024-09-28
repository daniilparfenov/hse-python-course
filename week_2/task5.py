"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/edit-distance/description
"""  # noqa: E501


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        table = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        table[0][0] = 0

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if j == 0 and i > 0:
                    table[i][j] = i
                elif i == 0 and j > 0:
                    table[i][j] = j
                elif i > 0 and j > 0:
                    table[i][j] = min(
                        table[i][j - 1] + 1,
                        table[i - 1][j] + 1,
                        table[i - 1][j - 1] + (word1[i - 1] != word2[j - 1]),
                    )
        return table[len(word1)][len(word2)]
