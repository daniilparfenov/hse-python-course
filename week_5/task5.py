"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/array-of-doubled-pairs/description
"""  # noqa: E501


class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False
        valX2 = dict()
        for num in sorted(arr, key=abs):
            if valX2.get(num) is not None:
                if valX2[num] > 0:
                    valX2[num] -= 1
                else:
                    if valX2.get(num * 2) is not None:
                        valX2[2 * num] += 1
                    else:
                        valX2[2 * num] = 1
            else:
                if valX2.get(num * 2) is not None:
                    valX2[2 * num] += 1
                else:
                    valX2[2 * num] = 1
        if all(i == 0 for i in valX2.values()):
            return True
        return False
