"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/binary-subarrays-with-sum
"""  # noqa: E501


class Solution:
    def numSubarrayWithSumLessOrEqualGoal(self, nums, goal):
        n = len(nums)
        result, cur_sum, left = 0, 0, 0
        for right in range(n):
            cur_sum += nums[right]

            while cur_sum > goal and left <= right:
                cur_sum -= nums[left]
                left += 1
            result += right - left + 1
        return result

    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count1 = self.numSubarrayWithSumLessOrEqualGoal(nums, goal)
        count2 = self.numSubarrayWithSumLessOrEqualGoal(nums, goal - 1)
        return count1 - count2
