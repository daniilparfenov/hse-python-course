"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/rotate-array/description
"""  # noqa: E501


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rotated = [0] * n
        k %= n

        for i in range(n):
            rotated[(i + k) % n] = nums[i]
        for i in range(n):
            nums[i] = rotated[i]
