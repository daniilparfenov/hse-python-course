"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/integer-to-roman/description/
"""  # noqa: E501


class Solution:
    def intToRoman(self, num: int) -> str:
        romanInterpretationOfNum = ""
        digitsOfNum = [int(digit) for digit in str(num)]
        while len(digitsOfNum) < 4:
            digitsOfNum = [0] + digitsOfNum

        romanInterpretationOfNum = "M" * digitsOfNum[0]

        if digitsOfNum[1] == 9:
            romanInterpretationOfNum += "CM"
        elif digitsOfNum[1] == 4:
            romanInterpretationOfNum += "CD"
        else:
            romanInterpretationOfNum += "D" * (digitsOfNum[1] // 5)
            digitsOfNum[1] %= 5
            romanInterpretationOfNum += "C" * digitsOfNum[1]

        if digitsOfNum[2] == 9:
            romanInterpretationOfNum += "XC"
        elif digitsOfNum[2] == 4:
            romanInterpretationOfNum += "XL"
        else:
            romanInterpretationOfNum += "L" * (digitsOfNum[2] // 5)
            digitsOfNum[2] %= 5
            romanInterpretationOfNum += "X" * digitsOfNum[2]

        if digitsOfNum[3] == 9:
            romanInterpretationOfNum += "IX"
        elif digitsOfNum[3] == 4:
            romanInterpretationOfNum += "IV"
        else:
            romanInterpretationOfNum += "V" * (digitsOfNum[3] // 5)
            digitsOfNum[3] %= 5
            romanInterpretationOfNum += "I" * digitsOfNum[3]

        return romanInterpretationOfNum
