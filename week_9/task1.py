"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/recover-binary-search-tree
"""  # noqa: E501

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, root, order):
        if root is None:
            return
        self.inorder(root.left, order)
        order.append(root)
        self.inorder(root.right, order)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        order = []
        self.inorder(root, order)

        fake_nodes = []
        for i in range(1, len(order)):
            if order[i].val < order[i - 1].val:
                fake_nodes.append(order[i - 1])
                fake_nodes.append(order[i])
        fake_nodes[0].val, fake_nodes[-1].val = fake_nodes[-1].val, fake_nodes[0].val
