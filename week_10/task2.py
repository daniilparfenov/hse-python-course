"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/sum-root-to-leaf-numbers
"""  # noqa: E501


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        right_side = []
        queue = [root]

        while queue:
            n = len(queue)
            for i in range(n):
                cur_node = queue.pop(0)
                if i == n - 1:
                    right_side.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
        return right_side
