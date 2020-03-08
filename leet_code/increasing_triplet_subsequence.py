"""
Given an unsorted array return whether an increasing subsequence of
length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1)
space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
"""


class Solution1:

    def _usingConstSpace(self, nums, sz):
        min1 = 0
        min2 = None
        for i in range(1, sz):
            if nums[i] < nums[min1]:
                min1 = i
            elif nums[i] > nums[min1] and (
                    min2 is None or nums[i] < nums[min2]):
                min2 = i
            elif min2 and nums[i] > nums[min2]:
                return True
        return False

    def _usingAuxSpace(self, nums, sz):
        dp1 = [0] * sz
        dp2 = [0] * sz
        smallest = 0
        dp1[0] = -1
        for i in range(1, sz):
            if nums[i] <= nums[smallest]:
                dp1[i] = -1
                smallest = i
            else:
                dp1[i] = smallest

        greatest = sz - 1
        dp2[sz - 1] = -1
        for i in range(sz - 1, 0, -1):
            if nums[i - 1] >= nums[greatest]:
                dp2[i - 1] = -1
                greatest = i - 1
            else:
                dp2[i - 1] = greatest

        for i in range(sz):
            if dp1[i] != -1 and dp2[i] != -1:
                return True
        return False

    def increasingTriplet(self, nums) -> bool:
        list_sz = len(nums)
        if list_sz < 2:
            return False

        return self._usingAuxSpace(nums, list_sz)