"""
Given a string, find the first non-repeating character in it and return
it's index. If it doesn't exist, return -1.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        str_freq_dict = Counter(s)
        for index, char in enumerate(s):
            if str_freq_dict.get(char) == 1:
                return index
        return -1
