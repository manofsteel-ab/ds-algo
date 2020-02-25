"""
Given an integer array nums, find the contiguous subarray (containing at least
 one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        current_sum = nums[0]
        ans = current_sum
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum+nums[i])
            ans = max(ans, current_sum)
        return ans