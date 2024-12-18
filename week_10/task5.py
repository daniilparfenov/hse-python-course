"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/kth-smallest-element-in-a-bst
"""  # noqa: E501

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, node, path):
        if not node:
            return
        self.inorder(node.left, path)
        path.append(node.val)
        self.inorder(node.right, path)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        path = []
        self.inorder(root, path)
        return path[k - 1]
