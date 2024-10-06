"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/combination-sum/description
"""  # noqa: E501


class Solution:
    def combination(self, curComb, curIndex, target, canditates, ans):
        if sum(curComb) > target or curIndex >= len(canditates):
            return
        if sum(curComb) == target:
            ans.append(curComb.copy())
            return
        for i in range(curIndex, len(canditates)):
            curComb.append(canditates[i])
            self.combination(curComb, i, target, canditates, ans)
            curComb.pop()

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        self.combination([], 0, target, candidates, ans)
        return ans
