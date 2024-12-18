"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/flatten-binary-tree-to-linked-list
"""  # noqa: E501

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    previous = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.previous
        root.left = None
        self.previous = root
