"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/valid-sudoku/description
"""  # noqa: E501


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [[] for i in range(len(board))]
        columns = [[] for j in range(len(board[0]))]
        boxes = {}

        for i in range(3):
            for j in range(3):
                boxes[(i, j)] = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if (
                    board[i][j] in rows[i]
                    or board[i][j] in columns[j]
                    or board[i][j] in boxes[(i // 3, j // 3)]
                ):
                    return False
                else:
                    rows[i].append(board[i][j])
                    columns[j].append(board[i][j])
                    boxes[(i // 3, j // 3)].append(board[i][j])
        return True
