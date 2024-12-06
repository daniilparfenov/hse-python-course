"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/substring-with-concatenation-of-all-words
"""  # noqa: E501

from collections import defaultdict


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        ans = []
        word_length = len(words[0])
        ref_word_freq = defaultdict(int)
        for word in words:
            ref_word_freq[word] += 1

        for offset in range(word_length):
            window_word_freq = defaultdict(int)
            window_size = 0
            for i in range(offset, len(s) - word_length + 1, word_length):
                word = s[i : i + word_length]
                if ref_word_freq.get(word) is None:
                    window_word_freq.clear()
                    window_size = 0
                    continue
                window_size += 1
                window_word_freq[word] += 1
                while window_word_freq[word] > ref_word_freq[word]:
                    first_word_in_window_index = i - (window_size - 1) * word_length
                    first_word_in_window = s[
                        first_word_in_window_index : first_word_in_window_index
                        + word_length
                    ]
                    window_size -= 1
                    window_word_freq[first_word_in_window] -= 1
                if window_size == len(words):
                    ans.append(i - (window_size - 1) * word_length)
        return ans
