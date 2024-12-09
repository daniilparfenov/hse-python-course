"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/fruit-into-baskets
"""  # noqa: E501

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        levels = []

        while queue:
            level = []
            cur_queue_size = len(queue)
            for i in range(cur_queue_size):
                cur_node = queue.pop(0)
                level.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            levels.append(level)
        return levels[::-1]
