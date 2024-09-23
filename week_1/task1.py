"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""  # noqa: E501


def decartProduce(lst1, lst2):
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1
    return [str(l1) + str(l2) for l1 in lst1 for l2 in lst2]


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digitToLetter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combinations = []
        for digit in digits:
            combinations = decartProduce(combinations, list(digitToLetter[digit]))
        return combinations
