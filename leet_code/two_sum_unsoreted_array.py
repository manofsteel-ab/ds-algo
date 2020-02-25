"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.
"""


import operator


class Solution:
    def twoSum(self, nums, target: int):
        start = 0
        end = len(nums) - 1
        element_index_pairs = []
        for index, val in enumerate(nums):
            element_index_pairs.append({
                'val': val, 'index': index
            })
        element_index_pairs.sort(key = operator.itemgetter('val'))

        while start < end:
            if element_index_pairs[start]['val'] + element_index_pairs[end][
                'val'] == target:
                return [element_index_pairs[start]['index'],
                    element_index_pairs[end]['index']]
            if element_index_pairs[start]['val'] + element_index_pairs[end][
                'val'] < target:
                start += 1
            else:
                end -= 1
        return []
