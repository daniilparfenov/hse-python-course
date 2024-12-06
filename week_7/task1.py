"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/minimum-window-substring
"""  # noqa: E501

from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map = defaultdict(int)
        tc = len(t)
        min_win = [0, 10**10]
        start_i = 0

        for c in t:
            map[c] += 1

        for end_i in range(len(s)):
            if map[s[end_i]] > 0:
                tc -= 1
            map[s[end_i]] -= 1

            if tc == 0:
                while True:
                    if map[s[start_i]] == 0:
                        break
                    map[s[start_i]] += 1
                    start_i += 1
                if end_i - start_i < min_win[1] - min_win[0]:
                    min_win[0] = start_i
                    min_win[1] = end_i
                map[s[start_i]] += 1
                tc += 1
                start_i += 1

        return s[min_win[0] : min_win[1] + 1] if min_win[1] != 10**10 else ""
