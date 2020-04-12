"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

"""


class Solution:

    def _bruteForce(self, x):
        ans = 1
        for i in range(2, x + 1 // 2):
            if i * i > x:
                break
            else:
                ans = i
        return ans

    def _binarySearch(self, low, high, x):
        if low >= high:
            return low

        while low <= high:
            mid = high + (low - high) // 2;
            if mid == x // mid:
                return mid
            elif (mid < x // mid):
                low = mid + 1
            else:
                high = mid - 1
        return min(low, high)

    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x <= 2:
            return 1
        return self._binarySearch(1, x, x)
