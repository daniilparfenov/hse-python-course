"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/frequency-of-the-most-frequent-element
"""  # noqa: E501


class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left, right, result, sum_ = 0, 0, 0, 0

        for right in range(n):
            sum_ += nums[right]

            while nums[right] * (right - left + 1) > sum_ + k:
                sum_ -= nums[left]
                left += 1
            result = max(result, right - left + 1)
        return result
