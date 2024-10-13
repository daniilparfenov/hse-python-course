"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/maximum-subarray/description
"""  # noqa: E501


class Solution:
    def findMaxMiddleSubArray(self, nums, left, right):
        mid = (left + right) // 2
        curSum = 0
        maxLeftSum = maxRightSum = -(10**10)

        for i in range(mid, left - 1, -1):
            curSum += nums[i]
            if curSum >= maxLeftSum:
                maxLeftSum = curSum

        curSum = 0
        for i in range(mid + 1, right + 1):
            curSum += nums[i]
            if curSum >= maxRightSum:
                maxRightSum = curSum
        return max(maxLeftSum, maxRightSum, maxLeftSum + maxRightSum)

    def findMaxSubArray(self, nums, left, right):
        if left > right:
            return -(10**10)
        if left == right:
            return nums[left]

        mid = (left + right) // 2
        maxLeftSum = self.findMaxSubArray(nums, left, mid - 1)
        maxMidSum = self.findMaxMiddleSubArray(nums, left, right)
        maxRightSum = self.findMaxSubArray(nums, mid + 1, right)

        return max(maxLeftSum, maxMidSum, maxRightSum)

    def maxSubArray(self, nums: list[int]) -> int:
        return self.findMaxSubArray(nums, 0, len(nums) - 1)
