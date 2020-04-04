"""
Given a set of distinct integers, nums, return all possible subsets
(the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:

    def _power(self, a, b):
        """return a^b b can be negative also"""
        if b == 0:
            return 1
        temp = self._power(a, int(b / 2))
        if b % 2 == 0:
            return temp * temp
        else:
            if b > 0:
                return a * temp * temp
            else:
                return temp * temp / a

    def subsets(self, nums):
        nums_sz = len(nums)
        total_possibilities = self._power(2, nums_sz)

        ans = []

        i = 0

        while i < total_possibilities:
            picked_elements = []
            if i == 0:
                ans.append(picked_elements)
            else:
                for j in range(nums_sz):
                    if i & 1 << j:
                        picked_elements.append(nums[j])
                ans.append(picked_elements)

            i += 1

        return ans


class Solution2:
    def subsets(self, nums):
        n = len(nums)
        output = []

        for i in range(2 ** n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output