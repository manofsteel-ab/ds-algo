"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums):
        from collections import Counter
        element_freq = Counter(nums)
        for key in element_freq:
            if element_freq[key] > 1:
                return True
        return False
