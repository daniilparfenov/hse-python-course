"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/triangle/description
"""  # noqa: E501


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        path = [[]]
        path[0].append(triangle[0][0])
        for i in range(1, len(triangle)):
            path.append([])
            for j in range(len(triangle[i])):
                path[i].append(10**10)
                if j - 1 >= 0:
                    path[i][j] = triangle[i][j] + path[i - 1][j - 1]
                if j < len(path[i - 1]):
                    path[i][j] = min(path[i][j], path[i - 1][j] + triangle[i][j])
        return min(path[-1])
