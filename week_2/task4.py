"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/zigzag-conversion/description
"""  # noqa: E501


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        table = [[] for i in range(numRows)]

        curRow = 0
        goDown = False
        for symbol in s:
            if curRow < numRows and not goDown:
                table[curRow].append(symbol)
                curRow += 1
            elif (curRow == numRows) or goDown:
                goDown = True
                if curRow == numRows:
                    table[curRow - 1].append(" ")
                    curRow -= 2
                else:
                    curRow -= 1
                if curRow != numRows - 2:
                    table[curRow].append(" ")
                table[curRow].append(symbol)
                if curRow == 0:
                    goDown = False
                    curRow = 1

        res = ""
        for line in table:
            for symbol in line:
                if symbol != " ":
                    res += symbol
        return res
