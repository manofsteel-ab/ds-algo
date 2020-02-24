"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any
positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which
this process ends in 1 are happy numbers.

Approach-
A number will not be a Happy Number when it makes a loop in its sequence
that is it touches a number in sequence which already been touched.
"""


class Solution:
    def sumOfSquareOfDigit(self, num):
        total = 0
        while num:
            total += (num % 10) * (num % 10)
            num = num // 10
        return total

    def isHappy(self, n: int) -> bool:
        slowP = n
        fastP = n
        while True:
            slowP = self.sumOfSquareOfDigit(slowP)
            fastP = self.sumOfSquareOfDigit(self.sumOfSquareOfDigit(fastP))
            if slowP == fastP:
                break
        return slowP == 1