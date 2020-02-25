"""
Given a non-empty array of digits representing a non-negative integer,
plus one to the integer.

The digits are stored such that the most significant digit is at the head of
the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the
number 0 itself.
"""


class Solution:
    def plusOne(self, digits):

        ans = ""
        total_digits = len(digits)

        current_index = total_digits - 1
        carry = 1
        while current_index >= 0:
            digit = (digits[current_index] + carry)
            carry = digit // 10
            ans = str(digit % 10) + ans
            current_index -= 1

        if carry == 1:
            ans = str(carry) + ans
        return ans
