"""
Calculate the sum of two integers a and b, but you are not allowed to use
the operator + and -.
"""


class Solution:
    def _add(self, a, b):
        if not b:
            return a
        if not a:
            return b
        carry = a & b
        a = a ^ b
        b = carry << 1
        return self._add(a, b)

    def _substract(self, a, b):
        if not b:
            return a
        if not a:
            return b
        borrow = (~a) & b
        a = a ^ b
        b = borrow << 1
        return self._substract(a, b)

    def getSum(self, a: int, b: int) -> int:
        if a >= 0 and b >= 0:
            return self._add(a, b)
        elif a < 0 and b < 0:
            return -self._add(-a, -b)
        elif a > 0 and b < 0:
            b = -b
            if b > a:
                return -self._substract(b, a)
            return self._substract(a, b)
        if a < 0 and b > 0:
            a = -a
            if a > b:
                return -self._substract(a, b)
            return self._substract(b, a)
