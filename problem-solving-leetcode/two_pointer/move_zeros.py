"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.
"""


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums)
        next_non_zero_idx = -1

        while start < end:
            if nums[start] != 0:
                start = start + 1
            else:
                if next_non_zero_idx == -1:
                    next_non_zero_idx = start + 1
                while next_non_zero_idx < end and nums[next_non_zero_idx] == 0:
                    next_non_zero_idx = next_non_zero_idx + 1
                # print(start,next_non_zero_idx)
                if next_non_zero_idx < end:
                    nums[start], nums[next_non_zero_idx] = nums[
                        next_non_zero_idx], nums[start]
                    start = start + 1
                else:
                    break

        return nums



