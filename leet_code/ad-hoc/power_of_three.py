"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
"""
import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n < 1:
            return False

        _multiple_of_three = 1

        while _multiple_of_three <= n:
            if _multiple_of_three == n:
                return True
            _multiple_of_three = _multiple_of_three * 3
        return False


class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        res = (math.log10(n)/math.log10(3))
        return res.is_integer()