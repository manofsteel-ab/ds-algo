"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
"""


class Solution:
    def intersect(self, nums1, nums2):
        from collections import Counter
        nums1_freq_dict = Counter(nums1)
        intersected_list = []
        for item in nums2:
            if nums1_freq_dict.get(item):
                intersected_list.append(item)
                nums1_freq_dict[item] -= 1
        return intersected_list
