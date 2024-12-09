"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-k-closest-elements
"""  # noqa: E501


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        left, right = 0, len(arr) - 1
        while right - left >= k:
            if abs(x - arr[left]) > abs(x - arr[right]):
                left += 1
            else:
                right -= 1
        return arr[left : right + 1]
