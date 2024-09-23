"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/string-to-integer-atoi/description/
"""  # noqa: E501


class Solution:
    def myAtoi(self, s: str) -> int:
        result = ""

        for symbol in s:
            if symbol == " " and len(result) > 0:
                break
            if symbol == " ":
                continue
            if symbol in "+-":
                if len(result) > 0:
                    break
                result += symbol
                continue
            if not symbol.isdigit() and symbol not in "+-":
                break
            if symbol.isdigit():
                result += symbol
                continue

        if result == "" or result == "+" or result == "-":
            return 0
        result = int(result)
        if result < -(2**31):
            result = -(2**31)
        elif result > 2**31 - 1:
            result = 2**31 - 1
        return result
