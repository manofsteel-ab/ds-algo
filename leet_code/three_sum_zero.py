"""
Given an array nums of n integers, are there elements a, b, c in
nums such that a + b + c = 0? Find all unique triplets in the array
which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ln = len(nums)
        ans = []
        for i in range(0,ln-2):
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = ln-1
            while j<k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                elif total<0:
                    j+=1
                else:
                    k-=1

        return ans
