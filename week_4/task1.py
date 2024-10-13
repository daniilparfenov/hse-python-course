"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description
"""  # noqa: E501


class Solution:
    def binSearch(self, nums, target, isLeftSearch):
        idx = -1
        l = m = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                idx = m
                if isLeftSearch:
                    r = m - 1
                else:
                    l = m + 1
        return idx

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]
