"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/sum-root-to-leaf-numbers
"""  # noqa: E501

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node, s):
        if not node:
            return 0
        s = s * 10 + node.val
        if not (node.left or node.right):
            return s
        return self.dfs(node.left, s) + self.dfs(node.right, s)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
