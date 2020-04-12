"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:

    def _generatePermutation(self, nums, current_index, total_size, ans):
        if current_index == total_size:
            ans.append(nums[:])
        else:
            i = current_index
            while i <= total_size:
                nums[i], nums[current_index] = nums[current_index], nums[i]
                print(i, current_index, nums[:], total_size)
                self._generatePermutation(nums, current_index + 1, total_size,
                                          ans)
                nums[i], nums[current_index] = nums[current_index], nums[i]
                i += 1

    def permute(self, nums):
        ans = []
        nums_sz = len(nums)
        self._generatePermutation(nums, 0, nums_sz - 1, ans)
        return ans
