"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/combination-sum-ii/description/
"""  # noqa: E501


class Solution:
    def combination(self, curComb, curIndex, target, candidates, ans):
        if target == 0:
            ans.append(curComb.copy())
            return

        for i in range(curIndex, len(candidates)):
            if i != curIndex and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            curComb.append(candidates[i])
            self.combination(curComb, i + 1, target - candidates[i], candidates, ans)
            curComb.pop()

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        candidates.sort()
        self.combination([], 0, target, candidates, ans)
        return ans
