"""
Given a binary array, find the maximum length of a contiguous subarray with
equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
and 1.
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mapper = {}
        total = 0
        ans = 0
        for index,val in enumerate(nums):
            if val == 0:
                total+=-1
            else:
                total+=1
            if total == 0:
                ans = max(ans,index+1)
            elif mapper.get(total) is not None:
                ans = max(ans, index-mapper[total])
            else:
                mapper[total] = index
        return ans
