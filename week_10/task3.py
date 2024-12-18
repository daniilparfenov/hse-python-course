"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/path-sum-ii
"""  # noqa: E501

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node, s, path, res):
        if not node:
            return 0
        s -= node.val
        path.append(node.val)
        if node.left is None and node.right is None:
            if s == 0:
                res.append(path.copy())
        else:
            self.dfs(node.left, s, path, res)
            self.dfs(node.right, s, path, res)
        path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, [], res)
        return res
