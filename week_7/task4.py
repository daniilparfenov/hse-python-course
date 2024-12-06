"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/arithmetic-slices
"""  # noqa: E501


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        seq_lengths = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                seq_lengths[i] = seq_lengths[i - 1] + 1
        return sum(seq_lengths)
