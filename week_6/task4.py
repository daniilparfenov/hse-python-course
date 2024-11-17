"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/count-number-of-nice-subarrays
"""  # noqa: E501


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        nice_subarr_count = 0
        cur_odd_count = 0
        odd_count = [0] * (len(nums) + 1)
        odd_count[0] = 1

        for num in nums:
            if num % 2 != 0:
                cur_odd_count += 1
            if cur_odd_count >= k:
                nice_subarr_count += odd_count[cur_odd_count - k]
            odd_count[cur_odd_count] += 1
        return nice_subarr_count
