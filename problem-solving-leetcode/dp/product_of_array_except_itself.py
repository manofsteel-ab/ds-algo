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
    def productExceptSelf(self, nums):
        nums_cnt = len(nums)
        ans = [1] * nums_cnt

        product_from_start = 1
        product_from_end = 1

        for i in range(0, nums_cnt):
            element_1 = nums[i]
            element_2 = nums[nums_cnt - i - 1]
            ans[i] = ans[i] * product_from_start
            ans[nums_cnt - i - 1] = ans[nums_cnt - i - 1] * product_from_end

            product_from_end = product_from_end * element_2
            product_from_start = product_from_start * element_1
        return ans

