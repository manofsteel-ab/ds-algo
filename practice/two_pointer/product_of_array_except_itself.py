"""
Given an array nums of n integers where n > 1,  return an array output such
that output[i] is equal to the product of all the elements of nums except
nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does
not count as extra space for the purpose of space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        sz = len(nums)
        if sz<2:
            return nums

        result = [1]*sz

        left_product = 1
        right_prduct = 1

        for i in range(sz):
            result[i] *= left_product
            result[sz-i-1]*=right_prduct
            left_product*=nums[i]
            right_prduct*=nums[sz-i-1]
        return result
        
