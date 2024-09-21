"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/simplify-path/?envType=problem-list-v2&envId=string
"""  # noqa: E501


class Solution:
    def simplifyPath(self, path: str) -> str:
        symbolsOfPath = [
            symbol for symbol in path.split("/") if "/" not in symbol and symbol != ""
        ]
        resultPath = []
        for symbol in symbolsOfPath:
            if symbol == ".":
                continue
            elif symbol == "..":
                if len(resultPath) == 0:
                    continue
                else:
                    del resultPath[-1]
            else:
                resultPath.append(symbol)

        return "/" + "/".join(resultPath)
