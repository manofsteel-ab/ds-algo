"""
Given an array of size n, find the majority element. The majority element is
the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always
exist in the array.
"""


class Solution:
    def majorityElement(self, nums):
        majority_count = 1
        majority_element = nums[0]

        current_index = 1
        while current_index < len(nums):
            if nums[current_index] != majority_element:
                majority_count = majority_count - 1
            else:
                majority_count = majority_count + 1

            if majority_count <= 0:
                majority_count = 1
                majority_element = nums[current_index]
            current_index = current_index + 1

        return majority_element
