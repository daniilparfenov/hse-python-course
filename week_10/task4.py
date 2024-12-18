"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/populating-next-right-pointers-in-each-node
"""  # noqa: E501

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return root
        queue = [root]

        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if i == n - 1:
                    node.next = None
                else:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
