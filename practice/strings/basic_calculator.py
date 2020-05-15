"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, /
operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
"""
import math


class Solution:

    def calculate(self, s: str) -> int:
        result = []
        num = 0
        operators = "+-*/"
        sign = "+"
        for char in s + "+":
            if char == ' ':
                continue
            if char not in operators:
                num = num * 10 + int(char)
            if char in operators:
                if sign == "+":
                    result.append(num)
                if sign == '-':
                    result.append(-num)
                if sign == "*":
                    prev = result.pop()
                    result.append(prev * num)

                if sign == "/":
                    prev = result.pop()
                    result.append(math.trunc(prev / num))
                sign = char
                num = 0
        return sum(result)
