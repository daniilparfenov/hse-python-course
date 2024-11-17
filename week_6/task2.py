"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/repeated-dna-sequences
"""  # noqa: E501


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        reapeated_sequences = []
        seen_sequences = set()

        for start in range(len(s)):
            end = start + 10
            if end > len(s):
                break
            if s[start:end] not in seen_sequences:
                seen_sequences.add(s[start:end])
            elif s[start:end] not in reapeated_sequences:
                reapeated_sequences.append(s[start:end])
        return reapeated_sequences
