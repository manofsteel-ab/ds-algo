"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can
you climb to the top?

Note: Given n will be a positive integer.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        prev_1 = 2
        prev_2 = 3
        for i in range(4, n + 1):
            c = prev_1 + prev_2
            prev_1 = prev_2
            prev_2 = c

        return prev_2
