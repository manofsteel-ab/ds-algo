"""
Given an array nums, there is a sliding window of size k which is moving from
the very left of the array to the very right. You can only see the k numbers in
the window. Each time the sliding window moves right by one position. Return the
max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if not nums:
             return []

        queue = []
        ans = []

        for i in range(k):
            while queue and nums[queue[-1]]<nums[i]:
                    queue.pop()
            queue.append(i)
        ans.append(nums[queue[0]])
        # print(queue,ans)
        for i in range(k, len(nums)):
            if queue and i-queue[0]>=k:
                queue.pop(0)
            while queue and nums[queue[-1]]<nums[i]:
                queue.pop()
            queue.append(i)
            ans.append(nums[queue[0]])
        return ans
