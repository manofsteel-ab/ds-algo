"""
Given an array, rotate the array to the right by k steps, where k is
non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""


class Solution:

    def _rotate_1(self, nums, k, list_sz):
        list_sz = len(nums)
        k = k % list_sz

        while k > 0:
            last_element = nums[-1]
            for i in reversed(range(list_sz)):
                if i != 0:
                    nums[i] = nums[i - 1]
            nums[0] = last_element
            k -= 1

    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        list_sz = len(nums)
        k = k % list_sz

        nums.reverse()

        for i in range(0, k // 2):
            nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]

        start = k
        end = list_sz - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

