"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/fruit-into-baskets
"""  # noqa: E501

from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        fruit_baskets = defaultdict(int)  # Хранит количество фруктов вида i
        n = len(fruits)
        left, right = 0, 0
        for right in range(n):
            fruit_baskets[fruits[right]] += 1
            if len(fruit_baskets) > 2:
                fruit_baskets[fruits[left]] -= 1
                if fruit_baskets[fruits[left]] == 0:
                    fruit_baskets.pop(fruits[left])
                left += 1
        return right - left + 1
