"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/count-and-say/description
"""  # noqa: E501


class Solution:
    def RLE(self, string: str) -> str:
        counter = 0
        curSymbol = string[0]
        RLE_string = ""
        for symbol in string:
            if symbol == curSymbol:
                counter += 1
            else:
                RLE_string += str(counter) + curSymbol
                curSymbol = symbol
                counter = 1
        return RLE_string + str(counter) + curSymbol

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.RLE(self.countAndSay(n - 1))
