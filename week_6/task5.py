"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/minimum-size-subarray-sum
"""  # noqa: E501


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = right = 0
        min_length = 10**6
        cur_sum = 0

        while right != len(nums):
            cur_sum += nums[right]
            while cur_sum >= target:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                cur_sum -= nums[left]
                left += 1
            right += 1
        return min_length if min_length != 10**6 else 0
