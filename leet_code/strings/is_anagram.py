"""
Given two strings s and t , write a function to determine if t is an
anagram of s.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        if not s and not t:
            return True
        if not s or not t:
            return False
        d1 = Counter(s)
        d2 = Counter(t)
        return d1 == d2
