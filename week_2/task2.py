"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/text-justification/description
"""  # noqa: E501


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        justifiedText = []
        curLineWidth = 0
        curLine = []
        for word in words:
            if len(word) + curLineWidth <= maxWidth - len(curLine):
                curLine.append(word)
                curLineWidth += len(word)
            else:
                spaceLength = (maxWidth - curLineWidth) // (
                    (len(curLine) - 1) + (len(curLine) == 1)
                )
                curLineWidth += spaceLength * ((len(curLine) - 1) + (len(curLine) == 1))
                curWordForAddingSpace = 0
                while curLineWidth < maxWidth:
                    curLine[curWordForAddingSpace] += " "
                    curWordForAddingSpace += 1
                    curLineWidth += 1
                if len(curLine) == 1:
                    justifiedText.append(curLine[0] + " " * spaceLength)
                else:
                    justifiedText.append((" " * spaceLength).join(curLine))
                curLine = [word]
                curLineWidth = len(word)

        if len(curLine) > 0:
            justifiedText.append(
                " ".join(curLine) + " " * (maxWidth - len(" ".join(curLine)))
            )
        return justifiedText
