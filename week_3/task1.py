"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/median-of-two-sorted-arrays/description
"""  # noqa: E501


class Solution:
    def findMedianSortedArray(self, arr):
        medIndex = (len(arr) - 1) // 2
        if len(arr) % 2 == 0:
            return (arr[medIndex] + arr[medIndex + 1]) / 2
        else:
            return arr[medIndex]

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        if len(nums1) == 0:
            return self.findMedianSortedArray(nums2)
        if len(nums2) == 0:
            return self.findMedianSortedArray(nums1)

        n1 = n2 = 0
        mergeSize = len(nums1) + len(nums2)
        mergeCount = curAdded = 0
        res = 0

        while mergeCount != mergeSize:
            if n1 < len(nums1) and n2 < len(nums2) and nums1[n1] < nums2[n2]:
                curAdded = nums1[n1]
                n1 += 1
            elif n2 < len(nums2):
                curAdded = nums2[n2]
                n2 += 1
            elif n1 < len(nums1):
                curAdded = nums1[n1]
                n1 += 1
            mergeCount += 1
            if res != 0:
                res = (res + curAdded) / 2
                return res
            if mergeCount == mergeSize // 2 + mergeSize % 2:
                if mergeSize % 2 == 0:
                    res = curAdded
                    continue
                else:
                    return curAdded
        return res
