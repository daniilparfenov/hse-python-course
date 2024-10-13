"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description
"""  # noqa: E501


class Solution:
    def binSearch(self, nums, target, isLeftSearch):
        idx = -1
        left = mid = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                idx = mid
                if isLeftSearch:
                    right = mid - 1
                else:
                    left = mid + 1
        return idx

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]
