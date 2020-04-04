"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping
you from robbing each of them is that adjacent houses have security system
connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""


class Solution:
    def rob(self, nums) -> int:
        total_nums = len(nums)
        if total_nums == 0:
            return 0
        if total_nums == 1:
            return nums[0]

        excluding_max = nums[0]
        including_max = nums[1]

        current_index = 2
        ans = max(excluding_max, including_max)
        while current_index < total_nums:
            temp1 = excluding_max + nums[current_index]
            excluding_max = max(including_max, excluding_max)
            including_max = temp1
            ans = max(ans, excluding_max, including_max)
            current_index += 1
        return ans

